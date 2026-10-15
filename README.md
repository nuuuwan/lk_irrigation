# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_21:09:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Thawalama — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 21:09:02 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 21:08:49 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.047 |  |
| 2026-10-15 21:08:49 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 432.000 | 🔺 Rising |
| 2026-10-15 21:08:48 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | 432.000 | 🔺 Rising |
| 2026-10-15 21:08:11 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -252.000 |  |
| 2026-10-15 21:08:09 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | -252.000 |  |
| 2026-10-15 21:07:38 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:07:02 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 21:06:17 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.060 |  |
| 2026-10-15 21:05:49 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 21:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | 0.000 |  |
| 2026-10-15 21:05:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-10-15 21:05:03 | Urawa (Nilwala Ganga) | 2.72 | 🟡 Alert | -0.030 |  |
| 2026-10-15 21:04:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:04:56 | Pitabeddara (Nilwala Ganga) | 4.76 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-10-15 21:04:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:04:04 | Thawalama (Gin Ganga) | 4.06 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-10-15 21:03:37 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.049 |  |
| 2026-10-15 21:03:18 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-15 21:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 21:03:01 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-15 21:02:54 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-10-15 21:02:48 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 21:02:47 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | -0.041 |  |
| 2026-10-15 21:02:18 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:02:17 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:02:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:57 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 21:01:49 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-15 21:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:06 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-10-15 21:01:02 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 21:00:52 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | 0.095 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 20:04:22 | Panadugama (Nilwala Ganga) | 6.33 | 🟠 Minor Flood | 0.131 | 🔺 Rising |
| 2026-10-15 21:01:06 | Thalgahagoda (Nilwala Ganga) | 1.88 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-10-15 21:04:56 | Pitabeddara (Nilwala Ganga) | 4.76 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2026-10-15 21:04:04 | Thawalama (Gin Ganga) | 4.06 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-10-15 21:01:57 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 21:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | 0.000 |  |
| 2026-10-15 21:05:03 | Urawa (Nilwala Ganga) | 2.72 | 🟡 Alert | -0.030 |  |
| 2026-10-15 21:08:49 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 432.000 | 🔺 Rising |
| 2026-10-15 21:00:52 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 21:03:12 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-15 20:05:37 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-15 21:01:49 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-15 21:09:02 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 21:02:48 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 21:05:49 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 21:01:02 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 21:07:02 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 20:09:45 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 21:02:17 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:04:11 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:01:18 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:07:38 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:02:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:04:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:02:18 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-15 21:03:01 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-15 21:03:18 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-15 21:02:54 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-10-15 21:02:47 | Peradeniya (Mahaweli Ganga) | 3.03 | 🟢 Normal | -0.041 |  |
| 2026-10-15 21:08:49 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.047 |  |
| 2026-10-15 21:03:37 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.049 |  |
| 2026-10-15 21:06:17 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.060 |  |
| 2026-10-15 21:05:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-10-15 21:08:11 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -252.000 |  |

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)