# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_17:15:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 17:15:01 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:11:45 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:10:52 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:10:29 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:09:18 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:08:31 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 17:07:54 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:06:12 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-03-14 17:05:58 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-03-14 17:05:54 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-14 17:05:26 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:05:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.045 |  |
| 2026-03-14 17:04:55 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.026 |  |
| 2026-03-14 17:04:40 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:04:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 17:04:14 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.026 |  |
| 2026-03-14 17:04:07 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:03:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:03:41 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.075 |  |
| 2026-03-14 17:03:29 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-03-14 17:03:20 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:03:02 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-14 17:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:02:48 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.124 |  |
| 2026-03-14 17:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 17:02:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:02:15 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-03-14 17:01:46 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.091 |  |
| 2026-03-14 17:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:35 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:32 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:22 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:12 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-14 17:01:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:01 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 17:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 16:30:26 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 17:05:58 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-03-14 17:01:12 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-14 17:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 17:01:01 | Manampitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 17:05:54 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-14 17:02:15 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 17:08:31 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 17:04:19 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 17:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:32 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 15:05:02 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:05:26 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:11:45 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:02:57 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:11 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:03:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:02:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:07:54 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:15:01 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:35 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:01:22 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:09:18 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:10:52 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:10:29 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-03-14 17:03:20 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:04:07 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:04:40 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-14 17:03:29 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-03-14 17:04:55 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.026 |  |
| 2026-03-14 17:04:14 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.026 |  |
| 2026-03-14 17:06:12 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-03-14 17:03:02 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-03-14 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-03-14 17:05:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.045 |  |
| 2026-03-14 16:08:11 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.047 |  |
| 2026-03-14 17:03:41 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.075 |  |
| 2026-03-14 17:01:46 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.091 |  |
| 2026-03-14 17:02:48 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)