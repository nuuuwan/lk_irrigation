# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_23:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 23:10:06 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 23:09:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:08:58 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:07:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.029 |  |
| 2026-03-20 23:05:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 23:05:11 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:04:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-03-20 23:04:34 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:04:20 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:03:56 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-20 23:03:48 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:33 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:31 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 23:03:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-03-20 23:02:56 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:02:47 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:19 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-03-20 23:02:16 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:12 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 23:02:10 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:55 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:53 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:01:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-03-20 23:00:50 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:46 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.051 |  |
| 2026-03-20 23:00:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 23:02:19 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-03-20 23:04:34 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-03-20 23:03:31 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-20 23:05:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 23:03:56 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 23:02:12 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 22:04:46 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 23:10:06 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 23:00:50 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:07:16 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:01:53 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:08:58 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 22:06:16 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:48 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:16 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:43 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:06 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:47 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:33 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:02:10 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-03-20 23:09:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:04:34 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:55 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:02:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:05:11 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:04:20 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:02:56 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:17 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-03-20 23:07:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.029 |  |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-20 23:00:46 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.051 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 22:09:12 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)