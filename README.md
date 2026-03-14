# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_08:21:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 08:21:09 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-03-14 08:20:00 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 08:19:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.134 |  |
| 2026-03-14 08:15:33 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-14 08:12:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:12:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-03-14 08:07:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.099 |  |
| 2026-03-14 08:07:28 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 08:06:33 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.024 |  |
| 2026-03-14 08:06:14 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-03-14 08:05:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:04:32 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:04:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-03-14 08:04:14 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-03-14 08:03:50 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:03:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:03:44 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:03:28 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 08:03:20 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:03:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-03-14 08:02:54 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-03-14 08:02:49 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2026-03-14 08:02:48 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:02:45 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 08:02:30 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.013 |  |
| 2026-03-14 08:02:27 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-03-14 08:02:16 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:16 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-03-14 08:01:56 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:46 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.030 |  |
| 2026-03-14 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:01:17 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:15 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:09 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:00:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:00:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:56:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.134 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 08:03:28 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 08:07:28 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 08:00:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:03:44 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:01:09 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:03:20 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 08:20:00 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 08:02:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 08:02:16 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:00:52 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:12:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:00:28 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:16 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:03:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:02:45 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:05:56 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:04:32 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:56 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:17 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:15 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:03:50 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:02:48 | Glencourse (Kelani Ganga) | 9.07 | 🟢 Normal | -0.010 |  |
| 2026-03-14 08:15:33 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-03-14 08:02:27 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-03-14 08:02:30 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.013 |  |
| 2026-03-14 08:12:09 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-03-14 08:06:33 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.024 |  |
| 2026-03-14 08:06:14 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.028 |  |
| 2026-03-14 08:04:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2026-03-14 08:02:54 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-03-14 08:01:46 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.030 |  |
| 2026-03-14 08:04:14 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-03-14 08:21:09 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-03-14 08:02:49 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2026-03-14 08:03:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-03-14 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.080 |  |
| 2026-03-14 08:07:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.099 |  |
| 2026-03-14 08:19:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)