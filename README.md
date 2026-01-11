# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_21:20:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,019 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:10:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-11 21:08:14 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-01-11 21:07:42 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:06:48 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:06:00 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 21:05:50 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:05:48 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.029 |  |
| 2026-01-11 21:05:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 21:05:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-01-11 21:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:04:43 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:22 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:04:20 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:14 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:03:50 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:03:37 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-01-11 21:03:20 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-11 21:03:20 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:03:19 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-01-11 21:03:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-11 21:03:00 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:02:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-11 21:02:40 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:02:17 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:02:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-01-11 21:01:57 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:55 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:31 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:21 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:16 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:14 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:00:31 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-01-11 21:00:06 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 20:59:38 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 21:10:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-01-11 21:02:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 21:03:20 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:03:50 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:05:50 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 21:05:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 21:03:20 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-11 21:02:17 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:04:22 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:02:40 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:04:45 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 21:06:00 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:00:06 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:21 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:14 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:55 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:06:48 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:20 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:43 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:31 | Siyambalanduwa (Heda Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:01:57 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:07:42 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-11 21:08:14 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-01-11 21:01:14 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:16 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-11 21:00:31 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-01-11 21:03:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-01-11 21:05:48 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.029 |  |
| 2026-01-11 21:03:37 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-01-11 21:05:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-01-11 21:03:19 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-01-11 21:02:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)