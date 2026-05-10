# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_14:25:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,060 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 14:25:43 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.017 |  |
| 2026-05-10 14:21:03 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.054 |  |
| 2026-05-10 14:15:48 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-10 14:14:59 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:11:41 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-10 14:10:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-10 14:07:01 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.056 |  |
| 2026-05-10 14:06:12 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.009 |  |
| 2026-05-10 14:05:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:05:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:05:17 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.142 |  |
| 2026-05-10 14:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.03 | 🟢 Normal | -0.011 |  |
| 2026-05-10 14:04:44 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:04:29 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.087 |  |
| 2026-05-10 14:04:27 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-05-10 14:04:25 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-05-10 14:04:11 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.061 |  |
| 2026-05-10 14:04:03 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:03:46 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:03:38 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -72.000 |  |
| 2026-05-10 14:03:36 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -72.000 |  |
| 2026-05-10 14:03:11 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 14:03:03 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:02:43 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:02:39 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-10 14:02:29 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:02:27 | Katharagama (Menik Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-05-10 14:02:19 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.120 |  |
| 2026-05-10 14:02:15 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-10 14:02:05 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.040 |  |
| 2026-05-10 14:02:02 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.071 |  |
| 2026-05-10 14:01:54 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-05-10 14:01:40 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-10 14:01:31 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:01:00 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:00:58 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 14:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 14:00:33 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:00:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:47:45 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 14:02:39 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-10 14:15:48 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-10 14:00:58 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-10 14:10:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-10 14:11:41 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-10 14:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 14:03:11 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 14:04:44 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:00:33 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:04:03 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:03:46 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:01:00 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:05:24 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:02:29 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:01:54 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:00:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:01:31 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:14:59 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 14:06:12 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.009 |  |
| 2026-05-10 14:05:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:03:03 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:02:43 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-10 14:02:27 | Katharagama (Menik Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-05-10 14:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.03 | 🟢 Normal | -0.011 |  |
| 2026-05-10 14:04:27 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-05-10 14:25:43 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.017 |  |
| 2026-05-10 14:01:40 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-10 14:02:15 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-05-10 14:04:25 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-05-10 14:02:05 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.040 |  |
| 2026-05-10 14:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-05-10 14:21:03 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.054 |  |
| 2026-05-10 14:07:01 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.056 |  |
| 2026-05-10 14:04:11 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.061 |  |
| 2026-05-10 14:02:02 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.071 |  |
| 2026-05-10 14:04:29 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.087 |  |
| 2026-05-10 14:02:19 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.120 |  |
| 2026-05-10 14:05:17 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.142 |  |
| 2026-05-10 14:03:38 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)