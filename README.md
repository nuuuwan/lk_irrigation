# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_16:13:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,434 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 16:13:32 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:12:26 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.108 |  |
| 2026-05-17 16:11:27 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.038 |  |
| 2026-05-17 16:10:18 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.017 |  |
| 2026-05-17 16:09:44 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-05-17 16:08:14 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-17 16:07:47 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-05-17 16:07:22 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:07:11 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:07:09 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-05-17 16:06:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:06:38 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:06:20 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.029 |  |
| 2026-05-17 16:06:15 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:05:31 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-17 16:05:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | -0.029 |  |
| 2026-05-17 16:04:47 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-05-17 16:04:23 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:04:18 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:03:55 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:03:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:46 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-05-17 16:03:44 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:34 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:26 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 16:02:41 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:02:36 | Thanthirimale (Malwathu Oya) | 3.64 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:02:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:02:14 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-17 16:02:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:01:39 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:01:36 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:01:17 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.061 |  |
| 2026-05-17 16:00:33 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:00:28 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:00:24 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 16:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | -0.029 |  |
| 2026-05-17 16:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-17 16:02:14 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-17 16:03:26 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 15:10:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 16:03:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:01:39 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:07:11 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:06:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:07:22 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:00:28 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:44 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:02:41 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:05:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:00:24 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:34 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:01:36 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:13:32 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:02:06 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:08:14 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-17 16:06:38 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:04:18 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:02:36 | Thanthirimale (Malwathu Oya) | 3.64 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:04:23 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:06:15 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:00:33 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:00:25 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:03:55 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-05-17 16:10:18 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.017 |  |
| 2026-05-17 16:09:44 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-05-17 16:07:09 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-05-17 16:05:31 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-05-17 16:07:47 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-05-17 16:06:20 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.029 |  |
| 2026-05-17 16:04:47 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-05-17 16:11:27 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.038 |  |
| 2026-05-17 16:03:46 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-05-17 16:01:17 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.061 |  |
| 2026-05-17 16:12:26 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)