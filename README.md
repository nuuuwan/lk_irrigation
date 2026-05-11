# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_05:26:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 05:26:08 | Kuda Oya (Kirindi Oya) | 4.67 | 🟢 Normal | 9.057 | 🔺 Rising |
| 2026-05-11 05:25:51 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 4.865 | 🔺 Rising |
| 2026-05-11 05:25:14 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 4.865 | 🔺 Rising |
| 2026-05-11 05:25:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:17:56 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 1.587 | 🔺 Rising |
| 2026-05-11 05:17:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 05:17:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-11 05:13:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-05-11 05:12:53 | Kuda Oya (Kirindi Oya) | 2.67 | 🟢 Normal | 9.057 | 🔺 Rising |
| 2026-05-11 05:12:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-11 05:12:14 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-05-11 05:12:07 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-05-11 05:10:45 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 1.587 | 🔺 Rising |
| 2026-05-11 05:07:02 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:06:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-11 05:06:04 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-11 05:05:55 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-11 05:05:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:04:28 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:03:59 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-11 05:03:58 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-05-11 05:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.049 |  |
| 2026-05-11 05:03:31 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 05:03:20 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-05-11 05:03:18 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.038 |  |
| 2026-05-11 05:03:12 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 05:03:09 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 05:02:38 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-11 05:02:30 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 05:02:18 | Thanamalwila (Kirindi Oya) | 5.30 | 🟠 Minor Flood | -0.383 |  |
| 2026-05-11 05:02:10 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.040 |  |
| 2026-05-11 05:01:58 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-05-11 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-11 05:01:09 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -1.364 |  |
| 2026-05-11 05:00:13 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:42:55 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 1.587 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 05:02:18 | Thanamalwila (Kirindi Oya) | 5.30 | 🟠 Minor Flood | -0.383 |  |
| 2026-05-11 05:26:08 | Kuda Oya (Kirindi Oya) | 4.67 | 🟢 Normal | 9.057 | 🔺 Rising |
| 2026-05-11 05:25:51 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 4.865 | 🔺 Rising |
| 2026-05-11 05:17:56 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 1.587 | 🔺 Rising |
| 2026-05-11 05:03:20 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-05-11 05:12:07 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-05-11 05:13:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-05-11 05:17:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-11 05:06:04 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-05-11 05:05:55 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-11 05:03:31 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 05:12:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-11 04:19:26 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-11 05:03:12 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 05:03:09 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 05:02:30 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 05:17:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 04:03:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:05:00 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:25:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:00:13 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:04:28 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:07:02 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 05:12:14 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-05-11 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-11 05:03:59 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-11 05:02:38 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-11 05:06:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-05-11 04:02:39 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-11 05:03:58 | Dunamale (Aththanagalu Oya) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-05-11 05:01:58 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.029 |  |
| 2026-05-11 05:03:18 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.038 |  |
| 2026-05-11 05:02:10 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | -0.040 |  |
| 2026-05-11 05:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.049 |  |
| 2026-05-11 05:01:09 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -1.364 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)