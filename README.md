# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_06:33:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 06:33:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.001 |  |
| 2026-10-14 06:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | -0.038 |  |
| 2026-10-14 06:12:42 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.334 |  |
| 2026-10-14 06:10:19 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-14 06:10:01 | Rathnapura (Kalu Ganga) | 4.19 | 🟢 Normal | -0.063 |  |
| 2026-10-14 06:09:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:08:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:08:18 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.176 |  |
| 2026-10-14 06:07:43 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.037 |  |
| 2026-10-14 06:07:00 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 06:06:03 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:05:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:05:23 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 06:05:04 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.151 |  |
| 2026-10-14 06:04:32 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 06:04:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 06:04:06 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 06:03:58 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:03:58 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:03:26 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-14 06:03:23 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 06:03:09 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:03:07 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.011 |  |
| 2026-10-14 06:03:06 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-10-14 06:03:00 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-14 06:02:59 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.149 |  |
| 2026-10-14 06:02:52 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-10-14 06:02:52 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-14 06:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-10-14 06:02:32 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-14 06:02:22 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 06:02:21 | Magura (Kalu Ganga) | 5.42 | 🟡 Alert | 0.000 |  |
| 2026-10-14 06:02:07 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.011 |  |
| 2026-10-14 06:01:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:01:51 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:01:45 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-14 06:01:34 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:01:33 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-14 06:00:29 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:00:12 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 06:05:23 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 06:03:26 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-14 06:02:21 | Magura (Kalu Ganga) | 5.42 | 🟡 Alert | 0.000 |  |
| 2026-10-14 06:01:33 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-14 06:01:45 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-14 06:04:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-14 06:02:32 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-14 06:07:00 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 06:04:32 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 06:02:22 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 06:00:12 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 06:10:19 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-14 06:04:06 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 06:03:23 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 06:33:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.001 |  |
| 2026-10-14 06:01:34 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:01:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:05:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:00:29 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:09:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:03:58 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:08:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:06:03 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-14 06:01:51 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 06:03:00 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-14 06:03:07 | Hanwella (Kelani Ganga) | 3.19 | 🟢 Normal | -0.011 |  |
| 2026-10-14 06:02:07 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.011 |  |
| 2026-10-14 06:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.012 |  |
| 2026-10-14 06:02:52 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-10-14 06:02:52 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-10-14 06:07:43 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | -0.037 |  |
| 2026-10-14 06:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.85 | 🟢 Normal | -0.038 |  |
| 2026-10-14 06:03:06 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-10-14 06:10:01 | Rathnapura (Kalu Ganga) | 4.19 | 🟢 Normal | -0.063 |  |
| 2026-10-14 06:02:59 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.149 |  |
| 2026-10-14 06:05:04 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.151 |  |
| 2026-10-14 06:08:18 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.176 |  |
| 2026-10-14 06:12:42 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.334 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)