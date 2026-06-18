# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_04:30:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,262 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 04:30:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:18:06 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.016 |  |
| 2026-06-19 04:16:45 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:16:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.008 |  |
| 2026-06-19 04:15:08 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:14:52 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-06-19 04:13:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:12:42 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-06-19 04:08:26 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 04:07:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-19 04:06:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:06:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:05:58 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:05:54 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:05:35 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 04:05:27 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:05:05 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-06-19 04:04:50 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-19 04:04:00 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.020 |  |
| 2026-06-19 04:03:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:03:00 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:02:51 | Katharagama (Menik Ganga) | -0.42 | 🟢 Normal | -0.300 |  |
| 2026-06-19 04:02:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 04:02:40 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-06-19 04:02:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.045 |  |
| 2026-06-19 04:02:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 04:02:21 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-19 04:02:16 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.021 |  |
| 2026-06-19 04:01:13 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:01:03 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:01:02 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:00:50 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 04:07:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-19 04:02:21 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-19 04:08:26 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-19 04:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-19 04:02:41 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 04:05:35 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 04:02:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 03:05:46 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:01:02 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:00:50 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:30:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:06:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:01:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:05:54 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:01:13 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:05:58 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:03:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:01:03 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:13:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:15:08 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:06:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:16:45 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 04:16:25 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.008 |  |
| 2026-06-19 04:12:42 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-06-19 04:05:27 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:04:50 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:03:00 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:05:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-19 04:18:06 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.016 |  |
| 2026-06-19 04:04:00 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.020 |  |
| 2026-06-19 04:02:40 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-06-19 04:02:16 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.021 |  |
| 2026-06-19 04:05:05 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-19 04:02:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.045 |  |
| 2026-06-19 04:14:52 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-06-19 04:02:51 | Katharagama (Menik Ganga) | -0.42 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)