# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_20:14:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 20:14:35 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:12:37 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-05-17 20:10:53 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.066 |  |
| 2026-05-17 20:09:21 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 20:07:52 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 20:07:28 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.048 |  |
| 2026-05-17 20:06:23 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.013 |  |
| 2026-05-17 20:05:57 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:05:31 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.772 |  |
| 2026-05-17 20:05:24 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:05:15 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.019 |  |
| 2026-05-17 20:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 20:04:33 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-05-17 20:04:18 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:04:12 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:04:05 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:04:02 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.079 |  |
| 2026-05-17 20:03:49 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:03:38 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.078 |  |
| 2026-05-17 20:03:37 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-17 20:03:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:02:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.131 |  |
| 2026-05-17 20:02:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:02:26 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.051 |  |
| 2026-05-17 20:02:24 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:02:23 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:02:20 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:02:19 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-17 20:01:54 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:01:33 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-17 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:01:19 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:00:52 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 19:59:18 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.772 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 20:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 20:03:37 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-17 20:09:21 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 20:07:52 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 20:04:18 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:03:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:01:54 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:14:35 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:02:20 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:03:49 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:02:24 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 20:01:19 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-17 19:07:41 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-05-17 20:05:24 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:04:12 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:04:05 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:02:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:02:23 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:05:57 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:00:52 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 20:01:33 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-05-17 20:06:23 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.013 |  |
| 2026-05-17 20:12:37 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-05-17 20:05:15 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.019 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-17 20:02:19 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-17 20:04:33 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-05-17 20:07:28 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.048 |  |
| 2026-05-17 20:02:26 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.051 |  |
| 2026-05-17 19:05:02 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.051 |  |
| 2026-05-17 20:10:53 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.066 |  |
| 2026-05-17 20:03:38 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.078 |  |
| 2026-05-17 20:04:02 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.079 |  |
| 2026-05-17 20:02:51 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.131 |  |
| 2026-05-17 20:05:31 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.772 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)