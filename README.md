# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_16:19:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,109 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 16:19:29 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-05-20 16:18:02 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.016 |  |
| 2026-05-20 16:17:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-20 16:14:45 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:13:43 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:13:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 16:05:37 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-05-20 16:00:16 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-20 16:17:13 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-20 16:04:14 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-20 16:04:43 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-20 16:04:45 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-20 16:04:04 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-20 16:05:08 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 16:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 16:06:16 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 16:02:59 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 16:01:51 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 16:05:16 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-20 16:01:22 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:02:11 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:01:14 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:02:16 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:01:40 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:03:21 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:03:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:14:45 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:00:40 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:02:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:13:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-20 15:10:43 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:13:43 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:01:17 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-20 16:19:29 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-05-20 16:05:10 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:03:24 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:05:26 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:03:36 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:01:19 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:00:48 | Thanthirimale (Malwathu Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-20 16:00:42 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-05-20 16:01:38 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | -0.011 |  |
| 2026-05-20 16:18:02 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.016 |  |
| 2026-05-20 16:03:29 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-20 16:03:19 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)