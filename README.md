# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_05:19:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 05:19:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-06-14 05:15:35 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-14 05:13:57 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.019 |  |
| 2026-06-14 05:12:58 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.125 |  |
| 2026-06-14 05:10:21 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.092 |  |
| 2026-06-14 05:08:15 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:07:22 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.020 |  |
| 2026-06-14 05:06:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-06-14 05:06:00 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:05:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-06-14 05:05:27 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.049 |  |
| 2026-06-14 05:04:44 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-06-14 05:04:36 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:04:19 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.029 |  |
| 2026-06-14 05:04:03 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.087 |  |
| 2026-06-14 05:03:59 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-14 05:03:45 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-06-14 05:03:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:03:30 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:03:29 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.056 |  |
| 2026-06-14 05:03:23 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.103 |  |
| 2026-06-14 05:02:50 | Dunamale (Aththanagalu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:02:49 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.016 |  |
| 2026-06-14 05:02:33 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-06-14 05:01:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:01:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:00:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-14 05:00:55 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 04:37:46 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.092 |  |
| 2026-06-14 04:30:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 03:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 05:15:35 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-14 05:08:15 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:01:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:00:55 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:03:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:02:33 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:09:56 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:04:36 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:01:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:02:50 | Dunamale (Aththanagalu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:06:00 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:03:30 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 05:19:42 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-06-14 05:05:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-06-14 04:05:10 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-14 05:04:44 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-06-14 05:00:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-14 04:01:34 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-06-14 04:00:56 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.012 |  |
| 2026-06-14 05:02:49 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.016 |  |
| 2026-06-14 05:13:57 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.019 |  |
| 2026-06-14 05:07:22 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-14 05:03:45 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.023 |  |
| 2026-06-14 05:04:19 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.029 |  |
| 2026-06-14 05:06:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-06-14 05:03:59 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-06-14 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-14 05:05:27 | Glencourse (Kelani Ganga) | 11.53 | 🟢 Normal | -0.049 |  |
| 2026-06-14 05:03:29 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.056 |  |
| 2026-06-14 05:04:03 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.087 |  |
| 2026-06-14 05:10:21 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.092 |  |
| 2026-06-14 05:03:23 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.103 |  |
| 2026-06-14 05:12:58 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.125 |  |
| 2026-06-14 04:05:13 | Panadugama (Nilwala Ganga) | 0.41 | 🟢 Normal | -3.633 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)