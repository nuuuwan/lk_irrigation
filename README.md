# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_12:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 12:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:09:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:07:04 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:07:01 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-17 12:06:28 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:05:45 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:05:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:05:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-17 12:04:50 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-17 12:04:44 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:04:35 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.047 |  |
| 2026-03-17 12:04:24 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:04:15 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:58 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 12:03:50 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:47 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-03-17 12:03:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-17 12:03:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:32 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:17 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:03:05 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:50 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:49 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-03-17 12:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-17 12:02:29 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:02:12 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 12:02:11 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-17 12:02:11 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.041 |  |
| 2026-03-17 12:02:05 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:01 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:01:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:01:55 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-03-17 12:01:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-03-17 12:01:38 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-17 12:01:25 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.187 |  |
| 2026-03-17 12:01:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.087 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 12:03:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-17 12:05:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-17 12:01:38 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-17 12:07:01 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-17 12:02:11 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-17 12:02:12 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 12:03:58 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 12:02:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:05:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:35 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:01:22 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:29 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:05:45 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:50 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:50 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:32 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:05 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:05 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:07:04 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:09:12 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:03:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:04:15 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:01 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:04:44 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:03:17 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:06:28 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:04:24 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:04:50 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-17 12:01:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.021 |  |
| 2026-03-17 12:03:47 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-03-17 12:02:49 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-03-17 12:01:55 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-03-17 12:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-17 12:02:11 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.041 |  |
| 2026-03-17 12:04:35 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.047 |  |
| 2026-03-17 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.087 |  |
| 2026-03-17 12:01:25 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)