# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_10:09:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 10:09:16 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.097 |  |
| 2026-10-14 10:08:47 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.045 |  |
| 2026-10-14 10:07:56 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.018 |  |
| 2026-10-14 10:07:13 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:07:00 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.117 |  |
| 2026-10-14 10:06:53 | Magura (Kalu Ganga) | 5.31 | 🟡 Alert | -0.052 |  |
| 2026-10-14 10:06:17 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.055 |  |
| 2026-10-14 10:06:09 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:05:44 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-10-14 10:05:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:04:48 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | 0.278 | 🔺 Rising |
| 2026-10-14 10:04:33 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.021 |  |
| 2026-10-14 10:04:15 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:04:11 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-10-14 10:04:10 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.054 |  |
| 2026-10-14 10:04:08 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-14 10:03:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:03:58 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-10-14 10:03:57 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:03:32 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-10-14 10:03:17 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.020 |  |
| 2026-10-14 10:03:08 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:03:04 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:02:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:02:38 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:02:35 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-14 10:01:50 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 10:01:49 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-14 10:01:48 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | -0.028 |  |
| 2026-10-14 10:01:35 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:00:56 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:00:36 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 09:01:36 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 10:04:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | 0.278 | 🔺 Rising |
| 2026-10-14 10:01:48 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | -0.028 |  |
| 2026-10-14 10:06:53 | Magura (Kalu Ganga) | 5.31 | 🟡 Alert | -0.052 |  |
| 2026-10-14 10:01:49 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-14 10:01:50 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 10:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:03:57 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-14 09:02:02 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:01:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:07:13 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:05:29 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:02:38 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:04:15 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:03:04 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:03:58 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:04:48 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 10:02:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:00:56 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:01:35 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:06:09 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:03:08 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:00:36 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-14 10:03:32 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-10-14 10:07:56 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.018 |  |
| 2026-10-14 10:03:58 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-10-14 10:03:17 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.020 |  |
| 2026-10-14 10:04:33 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.021 |  |
| 2026-10-14 10:05:44 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-10-14 10:04:11 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-10-14 10:04:08 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-14 09:10:22 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-10-14 10:02:35 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-14 10:08:47 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.045 |  |
| 2026-10-14 10:04:10 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.054 |  |
| 2026-10-14 10:06:17 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.055 |  |
| 2026-10-14 10:09:16 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.097 |  |
| 2026-10-14 10:07:00 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)