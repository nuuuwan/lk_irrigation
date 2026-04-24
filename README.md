# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_22:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 22:17:29 | Wellawaya (Kirindi Oya) | 0.18 | 🟢 Normal | -8.018 |  |
| 2026-04-24 22:17:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-04-24 22:13:52 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:12:21 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-04-24 22:10:00 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -8.018 |  |
| 2026-04-24 22:08:58 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.027 |  |
| 2026-04-24 22:08:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-24 22:07:18 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-04-24 22:06:46 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 22:06:40 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:06:33 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:06:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:05:47 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:05:41 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:05:31 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-04-24 22:05:08 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:05:05 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 22:04:19 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:04:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2026-04-24 22:04:06 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:03:46 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-24 22:03:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 86.087 | 🔺 Rising |
| 2026-04-24 22:02:50 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | 86.087 | 🔺 Rising |
| 2026-04-24 22:02:42 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-04-24 22:02:40 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.013 |  |
| 2026-04-24 22:02:40 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:02:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:02:08 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 22:01:48 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:01:48 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:01:32 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:01:19 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.031 |  |
| 2026-04-24 22:01:08 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:01:02 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:00:59 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-24 22:00:54 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:00:39 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 86.087 | 🔺 Rising |
| 2026-04-24 22:00:59 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-24 22:03:46 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-24 22:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-24 22:06:46 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 22:05:05 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 22:01:02 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:02:08 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:05:47 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:04:19 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:03:29 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:06:33 | Katharagama (Menik Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:06:08 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:13:52 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:01:32 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-24 22:12:21 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-04-24 22:07:18 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-04-24 22:05:08 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:02:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:05:41 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:01:48 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:00:54 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-24 22:02:40 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.013 |  |
| 2026-04-24 22:05:31 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-04-24 22:00:39 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-24 22:08:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-24 22:08:58 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.027 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-24 22:06:40 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:02:40 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:04:06 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-24 22:01:19 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | -0.031 |  |
| 2026-04-24 22:17:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.033 |  |
| 2026-04-24 22:02:42 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-04-24 22:04:14 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2026-04-24 20:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.071 |  |
| 2026-04-24 22:17:29 | Wellawaya (Kirindi Oya) | 0.18 | 🟢 Normal | -8.018 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)