# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_02:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 02:12:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-25 02:11:43 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:10:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-25 02:09:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:08:39 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:08:35 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:06:34 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 02:05:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -36.000 |  |
| 2026-03-25 02:05:15 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:05:15 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -36.000 |  |
| 2026-03-25 02:05:14 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-25 02:05:09 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:05:01 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-25 02:04:25 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:04:03 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:03:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-03-25 02:03:34 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:03:31 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:37 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:02:31 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:20 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:20 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:17 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.088 |  |
| 2026-03-25 02:02:10 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:01:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:01:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.040 |  |
| 2026-03-25 02:01:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:01:27 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:00:59 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:00:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 02:12:05 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-25 02:05:14 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-25 02:06:34 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 02:00:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:04:25 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:01:27 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 01:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:04:03 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-25 01:14:52 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:02:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:11:43 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:08:39 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:05:15 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:01:55 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:20 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:09:50 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:03:34 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:03:31 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:00:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:31 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:05:09 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:02:20 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:03:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.005 |  |
| 2026-03-25 01:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.008 |  |
| 2026-03-25 01:07:06 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | -0.009 |  |
| 2026-03-25 02:05:01 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-25 02:00:59 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:01:27 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:02:37 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.020 |  |
| 2026-03-25 02:02:10 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-25 00:03:36 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-03-25 02:01:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.040 |  |
| 2026-03-25 02:10:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-25 02:02:17 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.088 |  |
| 2026-03-24 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.120 |  |
| 2026-03-24 23:02:32 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.155 |  |
| 2026-03-25 02:05:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)