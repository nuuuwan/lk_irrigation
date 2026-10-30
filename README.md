# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_12:08:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,064 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 12:08:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:08:05 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:07:28 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | -0.041 |  |
| 2026-10-30 12:07:23 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.040 |  |
| 2026-10-30 12:07:21 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:06:00 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:05:47 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.066 |  |
| 2026-10-30 12:05:25 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.041 |  |
| 2026-10-30 12:04:30 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:04:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:04:21 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 12:04:04 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-30 12:04:03 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-30 12:03:50 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-30 12:03:36 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-10-30 12:03:28 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 12:03:24 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:03:15 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 12:02:57 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:02:44 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:02:40 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-30 12:02:25 | Putupaula (Kalu Ganga) | 3.34 | 🟡 Alert | -0.032 |  |
| 2026-10-30 12:02:24 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:02:23 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.033 |  |
| 2026-10-30 12:02:22 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 12:02:08 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-30 12:02:03 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:46 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-10-30 12:01:38 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:38 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-30 12:01:35 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:28 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:22 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-30 12:01:20 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:00:34 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.040 |  |
| 2026-10-30 12:00:26 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:00:22 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 12:03:15 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 12:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.60 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-30 12:02:25 | Putupaula (Kalu Ganga) | 3.34 | 🟡 Alert | -0.032 |  |
| 2026-10-30 12:05:25 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.041 |  |
| 2026-10-30 12:02:08 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-30 12:01:38 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-30 12:04:03 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-30 12:01:22 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-30 12:04:04 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-30 12:04:21 | Dunamale (Aththanagalu Oya) | 2.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 12:02:22 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 12:03:28 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 12:00:22 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:02:03 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:28 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:00:26 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:38 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:04:24 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:01:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:08:40 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:08:05 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:06:00 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:04:30 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:02:24 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:02:44 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-30 12:07:21 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:03:24 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:02:57 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:02:40 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-30 12:03:50 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-10-30 12:01:46 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-10-30 12:02:23 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.033 |  |
| 2026-10-30 12:00:34 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.040 |  |
| 2026-10-30 12:07:23 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | -0.040 |  |
| 2026-10-30 12:07:28 | Baddegama (Gin Ganga) | 3.38 | 🟢 Normal | -0.041 |  |
| 2026-10-30 12:03:36 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.050 |  |
| 2026-10-30 12:05:47 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)