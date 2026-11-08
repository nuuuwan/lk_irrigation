# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_08:24:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 08:24:09 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 08:16:39 | Pitabeddara (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:14:34 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:10:56 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-11-08 08:10:13 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:10:11 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:10:11 | Moragaswewa (Deduru Oya) | 2.60 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-08 08:09:43 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2026-11-08 08:08:00 | Baddegama (Gin Ganga) | 2.98 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 08:07:07 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | -0.054 |  |
| 2026-11-08 08:06:41 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.090 |  |
| 2026-11-08 08:05:46 | Moraketiya (Walawe Ganga) | 3.37 | 🟡 Alert | -0.060 |  |
| 2026-11-08 08:05:16 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.020 |  |
| 2026-11-08 08:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 08:05:01 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.159 |  |
| 2026-11-08 08:04:30 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-11-08 08:04:21 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.051 |  |
| 2026-11-08 08:04:03 | Pitabeddara (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:04:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-11-08 08:03:53 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.251 |  |
| 2026-11-08 08:03:42 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.249 |  |
| 2026-11-08 08:03:37 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.061 |  |
| 2026-11-08 08:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-11-08 08:03:16 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:03:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.136 |  |
| 2026-11-08 08:03:07 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-08 08:03:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.022 |  |
| 2026-11-08 08:02:45 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.050 |  |
| 2026-11-08 08:02:39 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.073 |  |
| 2026-11-08 08:02:33 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:02:29 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.101 |  |
| 2026-11-08 08:02:26 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 08:02:15 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.081 |  |
| 2026-11-08 08:02:09 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-08 08:02:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.100 |  |
| 2026-11-08 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:01:13 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:00:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:00:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 08:03:07 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.023 |  |
| 2026-11-08 08:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.37 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 08:05:16 | Dunamale (Aththanagalu Oya) | 3.70 | 🟡 Alert | -0.020 |  |
| 2026-11-08 08:07:07 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | -0.054 |  |
| 2026-11-08 08:05:46 | Moraketiya (Walawe Ganga) | 3.37 | 🟡 Alert | -0.060 |  |
| 2026-11-08 08:10:11 | Moragaswewa (Deduru Oya) | 2.60 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-08 08:02:09 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-08 08:08:00 | Baddegama (Gin Ganga) | 2.98 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 08:24:09 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 08:02:05 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-08 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:01:13 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:16:39 | Pitabeddara (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:10:13 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 08:10:56 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-11-08 08:00:32 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-08 08:02:29 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-08 08:14:34 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:00:56 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.017 |  |
| 2026-11-08 08:09:43 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2026-11-08 08:03:16 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:02:33 | Peradeniya (Mahaweli Ganga) | 3.16 | 🟢 Normal | -0.021 |  |
| 2026-11-08 08:03:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.022 |  |
| 2026-11-08 08:03:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-11-08 08:02:26 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-11-08 08:04:30 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.033 |  |
| 2026-11-08 08:02:45 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.050 |  |
| 2026-11-08 08:04:21 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.051 |  |
| 2026-11-08 08:04:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.058 |  |
| 2026-11-08 08:03:37 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.061 |  |
| 2026-11-08 08:02:39 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.073 |  |
| 2026-11-08 08:02:15 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.081 |  |
| 2026-11-08 08:06:41 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.090 |  |
| 2026-11-08 08:01:43 | Thanamalwila (Kirindi Oya) | 2.06 | 🟢 Normal | -0.100 |  |
| 2026-11-08 08:02:27 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.101 |  |
| 2026-11-08 08:03:08 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.136 |  |
| 2026-11-08 08:05:01 | Thawalama (Gin Ganga) | 2.81 | 🟢 Normal | -0.159 |  |
| 2026-11-08 08:03:42 | Kuda Oya (Kirindi Oya) | 2.11 | 🟢 Normal | -0.249 |  |
| 2026-11-08 08:03:53 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)