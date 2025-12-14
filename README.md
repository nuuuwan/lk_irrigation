# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_08:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,502 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 08:19:08 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:18:42 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -10.000 |  |
| 2025-12-14 08:14:30 | Weraganthota (Mahaweli Ganga) | -0.72 | 🟢 Normal | -10.000 |  |
| 2025-12-14 08:12:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:09:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:07:13 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.029 |  |
| 2025-12-14 08:07:03 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 08:06:40 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-14 08:05:56 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.095 |  |
| 2025-12-14 08:05:54 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 08:05:54 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:05:52 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.020 |  |
| 2025-12-14 08:05:41 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.031 |  |
| 2025-12-14 08:05:39 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 08:05:03 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2025-12-14 08:04:47 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:44 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-14 08:04:16 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:13 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:11 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:07 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-14 08:03:55 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 08:03:52 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:40 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:12 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2025-12-14 08:02:56 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-14 08:02:32 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:15 | Thanthirimale (Malwathu Oya) | 4.38 | 🟢 Normal | -0.024 |  |
| 2025-12-14 08:02:15 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:14 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:07 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.012 |  |
| 2025-12-14 08:01:40 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 08:01:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-14 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:01:23 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:00:59 | Horowpothana (Yan Oya) | 4.70 | 🟢 Normal | -0.090 |  |
| 2025-12-14 08:00:58 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:00:08 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 08:06:40 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-14 08:04:44 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-14 08:01:34 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-14 08:07:03 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-14 08:01:40 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-14 08:05:54 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-14 08:05:39 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-14 08:12:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:14 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:00:08 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:01:23 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:07 | Yaka Wewa (Ma Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:15 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:52 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:13 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:09:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:00:58 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:40 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:19:08 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:02:32 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:47 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:05:54 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:16 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:11 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2025-12-14 08:04:07 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-14 08:03:55 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-14 08:05:03 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2025-12-14 08:02:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.012 |  |
| 2025-12-14 08:05:52 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.020 |  |
| 2025-12-14 08:03:12 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2025-12-14 08:02:15 | Thanthirimale (Malwathu Oya) | 4.38 | 🟢 Normal | -0.024 |  |
| 2025-12-14 08:07:13 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.029 |  |
| 2025-12-14 08:02:56 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2025-12-14 08:05:41 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.031 |  |
| 2025-12-14 08:00:59 | Horowpothana (Yan Oya) | 4.70 | 🟢 Normal | -0.090 |  |
| 2025-12-14 08:05:56 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.095 |  |
| 2025-12-14 08:18:42 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -10.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)