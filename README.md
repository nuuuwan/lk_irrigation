# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_03:18:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 03:18:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:18:51 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:15:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:07:19 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-06-18 03:06:52 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-06-18 03:06:50 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.138 |  |
| 2026-06-18 03:06:24 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-18 03:06:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:06:18 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.528 |  |
| 2026-06-18 03:05:52 | Wellawaya (Kirindi Oya) | 0.32 | 🟢 Normal | -0.327 |  |
| 2026-06-18 03:05:49 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-18 03:05:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 03:05:41 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-18 03:05:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:05:07 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.218 |  |
| 2026-06-18 03:05:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 31.805 | 🔺 Rising |
| 2026-06-18 03:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:04:32 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-06-18 03:04:08 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-18 03:03:55 | Nagalagam Street (Kelani Ganga) | 0.06 | 🟢 Normal | 31.805 | 🔺 Rising |
| 2026-06-18 03:03:53 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:03:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 31.805 | 🔺 Rising |
| 2026-06-18 03:03:35 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.140 |  |
| 2026-06-18 03:03:27 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-18 03:03:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 31.805 | 🔺 Rising |
| 2026-06-18 03:03:15 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -2.028 |  |
| 2026-06-18 03:03:10 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 03:02:58 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:53 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 03:02:43 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:07 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -2.028 |  |
| 2026-06-18 03:01:58 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:00:58 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:00:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:00:48 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-18 02:53:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:50:16 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 03:05:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 31.805 | 🔺 Rising |
| 2026-06-18 03:03:27 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-18 03:05:49 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-18 03:00:48 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-18 03:05:41 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-18 03:06:24 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-18 03:04:08 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-18 00:12:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-18 03:05:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 03:03:10 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 03:02:53 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-18 03:06:21 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:00:58 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:02:06 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:03:53 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:03:15 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:07 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:53:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:05:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:58 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:01:58 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-18 02:16:39 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:18:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:02:43 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:15:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-18 03:07:19 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 03:06:52 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-06-18 03:04:32 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-06-18 03:06:50 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.138 |  |
| 2026-06-18 03:03:35 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.140 |  |
| 2026-06-18 03:05:07 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.218 |  |
| 2026-06-18 03:05:52 | Wellawaya (Kirindi Oya) | 0.32 | 🟢 Normal | -0.327 |  |
| 2026-06-18 03:06:18 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.528 |  |
| 2026-06-18 03:03:10 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -2.028 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)