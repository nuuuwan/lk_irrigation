# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_15:12:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 15:12:52 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:10:46 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 15:09:43 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:08:45 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:07:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-05-16 15:07:07 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-05-16 15:06:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.044 |  |
| 2026-05-16 15:06:35 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2026-05-16 15:06:10 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.019 |  |
| 2026-05-16 15:06:10 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.031 |  |
| 2026-05-16 15:05:51 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-16 15:05:48 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:05:35 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 15:05:19 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:05:06 | Galgamuwa (Mee Oya) | 3.10 | 🟢 Normal | -0.196 |  |
| 2026-05-16 15:04:54 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.029 |  |
| 2026-05-16 15:04:37 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:04:03 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-16 15:04:01 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-05-16 15:03:24 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:03:10 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 15:02:59 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:52 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | -0.107 |  |
| 2026-05-16 15:02:37 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | -0.063 |  |
| 2026-05-16 15:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:02:24 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:20 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.012 |  |
| 2026-05-16 15:02:13 | Thanthirimale (Malwathu Oya) | 3.92 | 🟢 Normal | -0.031 |  |
| 2026-05-16 15:02:12 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:02:10 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:02 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.023 |  |
| 2026-05-16 15:01:57 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:01:55 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-16 15:01:52 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:01:24 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:01:23 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:01:11 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-16 15:01:07 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.073 |  |
| 2026-05-16 15:00:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 15:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 15:02:52 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | -0.107 |  |
| 2026-05-16 15:07:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 5.455 | 🔺 Rising |
| 2026-05-16 15:04:03 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-16 15:01:55 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-16 15:10:46 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 15:05:35 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 15:05:48 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:01:23 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:05:19 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 15:01:52 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:24 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:03:24 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:08:45 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:12:52 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:01:57 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:04:37 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:03:10 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:59 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:02:10 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:00:21 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-16 15:09:43 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:02:12 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:01:24 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-05-16 15:02:20 | Moragaswewa (Deduru Oya) | 3.00 | 🟢 Normal | -0.012 |  |
| 2026-05-16 15:06:10 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.019 |  |
| 2026-05-16 15:05:51 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-16 15:01:11 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-16 15:02:02 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.023 |  |
| 2026-05-16 15:04:54 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.029 |  |
| 2026-05-16 15:06:35 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2026-05-16 15:06:10 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | -0.031 |  |
| 2026-05-16 15:02:13 | Thanthirimale (Malwathu Oya) | 3.92 | 🟢 Normal | -0.031 |  |
| 2026-05-16 15:06:37 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.044 |  |
| 2026-05-16 15:04:01 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-05-16 15:02:37 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | -0.063 |  |
| 2026-05-16 15:01:07 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.073 |  |
| 2026-05-16 15:05:06 | Galgamuwa (Mee Oya) | 3.10 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)