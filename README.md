# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_05:10:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 05:10:32 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.046 |  |
| 2026-10-18 05:07:44 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.099 |  |
| 2026-10-18 05:07:16 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-10-18 05:06:39 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-18 05:06:12 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -0.202 |  |
| 2026-10-18 05:06:08 | Thawalama (Gin Ganga) | 3.84 | 🟢 Normal | -0.059 |  |
| 2026-10-18 05:05:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-18 05:05:47 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-18 05:05:28 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-18 05:05:19 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.238 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 05:04:16 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 05:03:58 | Panadugama (Nilwala Ganga) | 6.14 | 🟠 Minor Flood | -0.179 |  |
| 2026-10-18 04:58:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.36 | 🟡 Alert | -0.316 |  |
| 2026-10-18 05:03:40 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | 0.480 | 🔺 Rising |
| 2026-10-18 05:05:52 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-10-18 05:03:30 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-18 05:05:47 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-18 05:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-18 05:03:45 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 05:04:16 | Horowpothana (Yan Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:14 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:01:14 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:03:44 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:03:02 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 05:04:11 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-17 21:21:56 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-10-18 05:03:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-18 03:04:52 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-18 05:03:16 | Hanwella (Kelani Ganga) | 4.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 04:02:26 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-18 05:05:28 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-18 05:01:02 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.017 |  |
| 2026-10-18 05:06:39 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-18 05:01:08 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-18 05:07:16 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-18 05:10:32 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.046 |  |
| 2026-10-18 05:06:08 | Thawalama (Gin Ganga) | 3.84 | 🟢 Normal | -0.059 |  |
| 2026-10-18 05:01:14 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:01:04 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-10-18 05:02:19 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.061 |  |
| 2026-10-18 05:07:44 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.099 |  |
| 2026-10-18 05:02:16 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.099 |  |
| 2026-10-18 05:06:12 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -0.202 |  |
| 2026-10-18 05:03:55 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.220 |  |
| 2026-10-18 05:03:30 | Glencourse (Kelani Ganga) | 12.34 | 🟢 Normal | -0.231 |  |
| 2026-10-18 05:05:19 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.238 |  |
| 2026-10-18 05:03:17 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.323 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)