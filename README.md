# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_10:27:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,160 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 10:27:05 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:10:54 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:09:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:09:10 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:08:00 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:07:44 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.029 |  |
| 2026-03-01 10:07:43 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:07:25 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.057 |  |
| 2026-03-01 10:07:25 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:07:02 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:06:37 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-01 10:06:26 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.057 |  |
| 2026-03-01 10:05:49 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-01 10:05:35 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:05:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:05:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-03-01 10:04:26 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.011 |  |
| 2026-03-01 10:04:24 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:04:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:04:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-01 10:03:57 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:03:53 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-01 10:03:38 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.022 |  |
| 2026-03-01 10:03:37 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:03:23 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-03-01 10:03:16 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 10:03:06 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 10:02:54 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-03-01 10:02:35 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-03-01 10:01:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:44 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:01:27 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:54 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:38 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 10:03:16 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 10:03:06 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 10:05:49 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-01 10:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:05:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:07:43 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:08:00 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 10:06:37 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-01 10:01:44 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:06 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:05:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:10:54 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:38 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:27 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:27:05 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:05:35 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:07:25 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:09:10 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:04:24 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:01:56 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:04:05 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:09:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:03:57 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:00:54 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:03:37 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:07:02 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 10:03:53 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-01 10:04:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-01 10:04:26 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.011 |  |
| 2026-03-01 10:03:38 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.022 |  |
| 2026-03-01 10:02:54 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.023 |  |
| 2026-03-01 10:03:23 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.024 |  |
| 2026-03-01 10:07:44 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.029 |  |
| 2026-03-01 10:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-03-01 10:02:35 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.041 |  |
| 2026-03-01 10:06:26 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.057 |  |
| 2026-03-01 10:07:25 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)