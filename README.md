# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_17:07:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,921 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 17:07:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-03-06 17:07:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:07:12 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:07:01 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:05:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:04:55 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.255 |  |
| 2026-03-06 17:04:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:34 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 17:03:23 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-06 17:03:22 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:09 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-06 17:03:07 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:02:55 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-06 17:02:54 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:02:52 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.055 |  |
| 2026-03-06 17:02:41 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-03-06 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 17:01:47 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:44 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:43 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:42 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:37 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-03-06 17:01:26 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-06 17:01:23 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:16 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:16 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-06 17:01:09 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:58 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-06 17:00:54 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:43 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-03-06 16:59:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-06 16:19:32 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 16:15:46 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 16:15:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 16:59:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-06 17:02:55 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-06 17:03:09 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-06 17:03:34 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 17:01:42 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:43 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:16 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 16:15:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:07 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:54 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:23 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:19 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:22 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:07:12 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 15:02:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:04:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 16:03:15 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:02:54 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:05:58 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:07:01 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:47 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:00:43 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:07:17 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-06 16:06:45 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:01:09 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 17:03:23 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-06 17:01:16 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-06 17:02:41 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-03-06 17:00:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-03-06 16:05:32 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.019 |  |
| 2026-03-06 17:01:37 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-03-06 17:01:26 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-06 17:00:58 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-06 17:02:52 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.055 |  |
| 2026-03-06 17:07:58 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-03-06 17:04:55 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.255 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)