# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_17:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,662 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 17:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:48 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.099 |  |
| 2026-11-15 17:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-15 17:02:24 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:02:23 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-11-15 17:02:16 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:09 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-11-15 17:02:03 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:59 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:01:48 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:35 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-11-15 17:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:00:49 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 16:07:46 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -0.028 |  |
| 2026-11-15 16:04:43 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-15 17:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-15 17:00:49 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-15 16:01:09 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 17:02:03 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:18:00 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:48 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:02:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:48 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:03:41 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:05:51 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:03:58 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:14 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:05:37 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:29 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:13:24 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-11-15 16:06:26 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:04:40 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:16 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:02:05 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:01:33 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-11-15 16:04:57 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-11-15 16:08:14 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-11-15 16:07:16 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | -0.019 |  |
| 2026-11-15 16:06:42 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.019 |  |
| 2026-11-15 16:13:21 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-15 16:04:17 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.019 |  |
| 2026-11-15 17:02:24 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:01:59 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:02:09 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-11-15 17:01:35 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-11-15 17:02:23 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-11-15 17:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)