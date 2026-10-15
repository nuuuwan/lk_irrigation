# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_20:10:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Thawalama — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 20:10:22 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 20:09:45 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 20:09:17 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-15 20:08:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:08:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 20:08:12 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-15 20:07:59 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 20:06:44 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:06:04 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.048 |  |
| 2026-10-15 20:06:01 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-15 20:06:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |
| 2026-10-15 20:05:44 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 20:05:37 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-15 20:05:34 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-10-15 20:05:24 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 20:04:22 | Panadugama (Nilwala Ganga) | 6.33 | 🟠 Minor Flood | 0.131 | 🔺 Rising |
| 2026-10-15 20:02:39 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-15 20:03:27 | Pitabeddara (Nilwala Ganga) | 4.68 | 🟡 Alert | 0.096 | 🔺 Rising |
| 2026-10-15 20:08:12 | Thawalama (Gin Ganga) | 4.02 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-15 20:03:04 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-15 20:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.010 |  |
| 2026-10-15 20:04:38 | Urawa (Nilwala Ganga) | 2.75 | 🟡 Alert | -0.164 |  |
| 2026-10-15 19:02:19 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-15 20:09:17 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-15 20:03:54 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 20:02:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 20:04:08 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 20:06:01 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-15 20:07:59 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 20:05:37 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-15 20:10:22 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 20:02:11 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 20:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 20:05:44 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 20:09:45 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 20:08:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 20:03:49 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:06:44 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:02:01 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:08:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:05:24 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:01:20 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 20:02:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-15 20:02:02 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.023 |  |
| 2026-10-15 19:04:39 | Ellagawa (Kalu Ganga) | 7.96 | 🟢 Normal | -0.028 |  |
| 2026-10-15 20:03:39 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | -0.030 |  |
| 2026-10-15 20:04:03 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-10-15 20:05:34 | Hanwella (Kelani Ganga) | 4.15 | 🟢 Normal | -0.030 |  |
| 2026-10-15 20:02:10 | Moraketiya (Walawe Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-10-15 20:06:04 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | -0.048 |  |
| 2026-10-15 20:06:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)