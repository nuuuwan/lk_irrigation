# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_19:19:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,506 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 19:19:37 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-06-13 19:19:35 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.017 |  |
| 2026-06-13 19:18:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-06-13 19:14:59 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 19:14:24 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-06-13 19:14:01 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.033 |  |
| 2026-06-13 19:11:13 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-06-13 19:08:56 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.036 |  |
| 2026-06-13 19:07:50 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 19:18:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-06-13 19:04:38 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-06-13 19:01:13 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-13 19:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-13 19:04:33 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-13 19:04:57 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 19:06:41 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 19:14:59 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-13 19:01:06 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:01:12 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:02:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:03:42 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:00:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:04:01 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:00:57 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:04:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:01:36 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-13 19:19:37 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-06-13 19:14:24 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-06-13 19:07:50 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:00:44 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:02:09 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:03:15 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.010 |  |
| 2026-06-13 19:02:27 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-06-13 19:19:35 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.017 |  |
| 2026-06-13 19:11:13 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-06-13 19:06:27 | Hanwella (Kelani Ganga) | 3.94 | 🟢 Normal | -0.019 |  |
| 2026-06-13 19:01:09 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-06-13 19:05:04 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | -0.021 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-13 19:00:58 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:00:22 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-06-13 19:14:01 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.033 |  |
| 2026-06-13 19:08:56 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.036 |  |
| 2026-06-13 19:02:55 | Giriulla (Maha Oya) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-13 19:05:59 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.067 |  |
| 2026-06-13 19:06:14 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)