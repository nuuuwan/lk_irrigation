# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_18:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,568 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 18:09:53 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:09:53 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:08:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:07:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-10 18:05:55 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:05:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:05:31 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:04:43 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-10 18:04:40 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-03-10 18:03:59 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:03:40 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:03:32 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:03:26 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:03:20 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:03:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:53 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |
| 2026-03-10 18:02:53 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-10 18:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-10 18:02:40 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:02:35 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-10 18:02:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:14 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:58 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:50 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:01:37 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:34 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:32 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:31 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:01:27 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:14 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-03-10 18:01:13 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-10 18:00:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-03-10 17:25:47 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-10 17:23:32 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.098 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 18:00:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-03-10 18:00:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-10 18:02:35 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-10 18:02:53 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-10 18:02:40 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:01:31 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:03:26 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 18:00:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:03:32 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:03:20 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:05:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 17:11:14 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:13 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:09:53 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:27 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:32 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:05:55 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:02:14 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:09:53 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:37 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:08:43 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:05:31 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:03:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:01:58 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:07:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-03-10 18:03:40 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:01:34 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:01:50 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:03:59 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 18:01:14 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-03-10 18:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-10 18:04:40 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-03-10 18:04:43 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-10 18:02:53 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)