# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_17:07:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 17:07:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:07:31 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:07:26 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.019 |  |
| 2026-05-17 17:06:34 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:05:35 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:05:02 | Magura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:04:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:04:48 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:39 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:17 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 17:04:03 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.046 |  |
| 2026-05-17 17:04:02 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:01 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:03:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.155 |  |
| 2026-05-17 17:03:41 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-17 17:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-17 17:03:32 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:03:21 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:03:20 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.023 |  |
| 2026-05-17 17:03:14 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-17 17:02:26 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:23 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:18 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.197 |  |
| 2026-05-17 17:02:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-17 17:02:09 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:09 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 17:02:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.278 |  |
| 2026-05-17 17:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:57 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.398 |  |
| 2026-05-17 17:01:54 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:48 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-17 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.078 |  |
| 2026-05-17 17:01:18 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 17:01:14 | Thanthirimale (Malwathu Oya) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:04 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:47:06 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.197 |  |
| 2026-05-17 16:25:02 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.197 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 17:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-17 17:03:14 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-17 17:02:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-17 17:02:09 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 17:01:18 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 17:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:07:52 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:02 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:04 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:54 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:26 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:03:44 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:39 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:04:48 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:00:24 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:09 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:03:21 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:01:14 | Thanthirimale (Malwathu Oya) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:03:32 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:13:32 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:02:23 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 16:08:14 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-17 17:04:17 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.010 |  |
| 2026-05-17 17:01:48 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-05-17 17:07:26 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.019 |  |
| 2026-05-17 17:07:31 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:04:58 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:05:35 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-05-17 17:03:41 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-17 17:03:20 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.023 |  |
| 2026-05-17 17:04:03 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.046 |  |
| 2026-05-17 17:06:34 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:04:01 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:05:02 | Magura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.067 |  |
| 2026-05-17 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.078 |  |
| 2026-05-17 17:03:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.155 |  |
| 2026-05-17 17:02:18 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.197 |  |
| 2026-05-17 17:02:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.278 |  |
| 2026-05-17 17:01:57 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.398 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)