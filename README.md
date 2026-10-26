# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_00:19:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,897 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Badalgama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 00:19:22 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.035 |  |
| 2026-10-27 00:18:29 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-27 00:17:42 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.085 | 🔺 Rising |
| 2026-10-27 00:13:01 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-27 00:11:16 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-27 00:10:36 | Rathnapura (Kalu Ganga) | 8.63 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-10-27 00:09:23 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | -0.182 |  |
| 2026-10-27 00:08:02 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:07:21 | Urawa (Nilwala Ganga) | 2.54 | 🟡 Alert | -0.019 |  |
| 2026-10-27 00:07:02 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:07:02 | Putupaula (Kalu Ganga) | 3.01 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-27 00:06:34 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-10-27 00:06:26 | Moragaswewa (Deduru Oya) | 4.72 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-27 00:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-10-27 00:05:58 | Hanwella (Kelani Ganga) | 6.71 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-27 00:05:36 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:05:29 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.235 |  |
| 2026-10-27 00:04:45 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:04:26 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:04:10 | Norwood (Kelani Ganga) | 1.84 | 🟡 Alert | -0.021 |  |
| 2026-10-27 00:04:09 | Giriulla (Maha Oya) | 5.14 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 00:04:04 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.078 |  |
| 2026-10-27 00:04:02 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:04:02 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:02:32 | Badalgama (Maha Oya) | 5.52 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-10-27 00:02:32 | Holombuwa (Kelani Ganga) | 2.96 | 🟢 Normal | -0.278 |  |
| 2026-10-27 00:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-27 00:02:29 | Dunamale (Aththanagalu Oya) | 4.54 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 00:02:25 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-10-27 00:02:11 | Glencourse (Kelani Ganga) | 15.15 | 🟡 Alert | -0.054 |  |
| 2026-10-27 00:02:08 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | -0.035 |  |
| 2026-10-27 00:02:07 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:01:55 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-27 00:01:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-10-27 00:01:17 | Moraketiya (Walawe Ganga) | 2.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-27 00:01:13 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 00:00:51 | Thawalama (Gin Ganga) | 5.27 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-10-27 00:00:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 00:17:42 | Panadugama (Nilwala Ganga) | 6.29 | 🟠 Minor Flood | 0.085 | 🔺 Rising |
| 2026-10-27 00:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-10-27 00:02:29 | Dunamale (Aththanagalu Oya) | 4.54 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 00:10:36 | Rathnapura (Kalu Ganga) | 8.63 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-10-27 00:02:32 | Badalgama (Maha Oya) | 5.52 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-10-27 00:00:51 | Thawalama (Gin Ganga) | 5.27 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-10-27 00:06:34 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-10-27 00:02:25 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-10-27 00:07:02 | Putupaula (Kalu Ganga) | 3.01 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-27 00:07:21 | Urawa (Nilwala Ganga) | 2.54 | 🟡 Alert | -0.019 |  |
| 2026-10-27 00:04:10 | Norwood (Kelani Ganga) | 1.84 | 🟡 Alert | -0.021 |  |
| 2026-10-27 00:19:22 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.035 |  |
| 2026-10-27 00:02:11 | Glencourse (Kelani Ganga) | 15.15 | 🟡 Alert | -0.054 |  |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 00:06:26 | Moragaswewa (Deduru Oya) | 4.72 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-27 00:04:09 | Giriulla (Maha Oya) | 5.14 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 00:05:58 | Hanwella (Kelani Ganga) | 6.71 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 00:11:16 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-27 00:18:29 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-27 00:02:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-27 00:01:17 | Moraketiya (Walawe Ganga) | 2.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-27 00:13:01 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-27 00:01:13 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 00:01:55 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-27 00:04:02 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:01:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 22:06:37 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:05:36 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:08:02 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:04:45 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:07:02 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-27 00:00:30 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.027 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 00:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-10-27 00:04:04 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.078 |  |
| 2026-10-27 00:09:23 | Peradeniya (Mahaweli Ganga) | 4.68 | 🟢 Normal | -0.182 |  |
| 2026-10-27 00:05:29 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.235 |  |
| 2026-10-27 00:02:32 | Holombuwa (Kelani Ganga) | 2.96 | 🟢 Normal | -0.278 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)