# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_19:20:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,716 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 19:20:18 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-30 19:11:49 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-30 19:10:41 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |
| 2026-06-30 19:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.063 |  |
| 2026-06-30 19:08:42 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-30 19:08:36 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.038 |  |
| 2026-06-30 19:08:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-30 19:07:11 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:06:11 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.028 |  |
| 2026-06-30 19:06:03 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.057 |  |
| 2026-06-30 19:05:37 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:05:14 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:04:09 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 19:04:06 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-06-30 19:03:57 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 19:03:50 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-06-30 19:03:38 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.019 |  |
| 2026-06-30 19:03:05 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:55 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:02:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-06-30 19:02:43 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:02:40 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-06-30 19:02:36 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:33 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-30 19:02:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:12 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:02:09 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-06-30 19:02:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:06 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:55 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-06-30 19:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:24 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-06-30 19:01:12 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 19:02:33 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-30 19:08:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-30 19:08:42 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-30 19:04:09 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 19:03:57 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 19:20:18 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-30 19:02:06 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:36 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:07:11 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:03:05 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:18 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:05:14 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:55 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:02:07 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:01:12 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:05:37 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 19:11:49 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-30 19:02:55 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:02:43 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:02:12 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:01:24 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-30 19:01:32 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-06-30 19:04:06 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-06-30 19:03:38 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | -0.019 |  |
| 2026-06-30 19:06:11 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.028 |  |
| 2026-06-30 19:03:50 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-06-30 19:08:36 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.038 |  |
| 2026-06-30 19:02:40 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-06-30 19:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-06-30 19:06:03 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.057 |  |
| 2026-06-30 19:02:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-06-30 19:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -0.063 |  |
| 2026-06-30 19:02:09 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-06-30 19:10:41 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)