# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_16:20:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 16:20:40 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:14:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.034 |  |
| 2026-04-22 16:12:18 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:11:09 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-22 16:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-04-22 16:08:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-22 16:07:55 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-22 16:07:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:07:11 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:06:53 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-04-22 16:06:10 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:05:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:05:44 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:05:36 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-04-22 16:05:31 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-04-22 16:05:06 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:05:05 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-04-22 16:04:57 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:04:42 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:04:18 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:04:02 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:03:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 16:03:48 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.050 |  |
| 2026-04-22 16:03:26 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:03:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-22 16:03:07 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.030 |  |
| 2026-04-22 16:03:05 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 16:02:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:02:50 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:02:49 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:02:13 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:02:13 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.044 |  |
| 2026-04-22 16:02:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 16:02:07 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:01:49 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 16:01:39 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-22 16:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:01:34 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.052 |  |
| 2026-04-22 16:01:20 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:01:05 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 16:00:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-04-22 16:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 16:05:31 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-04-22 16:05:36 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-04-22 16:03:19 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-22 16:01:39 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-22 16:02:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 16:03:59 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 16:07:55 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-22 16:08:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-22 16:01:05 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 16:03:05 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 16:01:49 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 16:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 16:04:57 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:07:11 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:05:06 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:04:18 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:02:07 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:02:13 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:12:18 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:20:40 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:05:05 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-04-22 16:05:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:02:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:04:02 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:01:20 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-22 16:11:09 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-04-22 16:03:26 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:04:42 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:02:49 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:07:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-22 16:06:53 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-04-22 16:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-04-22 16:03:07 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.030 |  |
| 2026-04-22 16:00:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-04-22 16:14:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.034 |  |
| 2026-04-22 16:02:13 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.044 |  |
| 2026-04-22 16:03:48 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.050 |  |
| 2026-04-22 16:01:34 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)