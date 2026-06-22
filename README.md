# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_05:15:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 05:15:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-06-22 05:13:27 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:12:20 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 05:12:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 05:10:23 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-22 05:09:38 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:09:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-06-22 05:08:24 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 05:08:13 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-22 05:07:55 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 05:07:52 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.045 |  |
| 2026-06-22 05:05:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:05:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:05:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:04:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:03:39 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:03:34 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-06-22 05:03:22 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:03:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:03:07 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.041 |  |
| 2026-06-22 05:02:59 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:02:54 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-06-22 05:02:49 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-22 05:02:43 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-22 05:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:02:32 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:02:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:02:16 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 05:01:35 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.012 |  |
| 2026-06-22 05:01:21 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.122 |  |
| 2026-06-22 05:01:19 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:01:17 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:00:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 04:47:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:46:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:41:15 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 04:47:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-06-22 04:14:53 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-06-22 05:02:49 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 05:02:16 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-22 05:02:43 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-22 05:08:13 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-22 05:07:55 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 05:10:23 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-22 05:12:10 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 05:12:20 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-22 05:00:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 05:08:24 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-22 05:03:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:13:27 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:05:50 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:02:59 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:04:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:01:17 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:05:59 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:05:22 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:02:32 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:09:38 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:01:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 05:09:27 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-06-22 05:15:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:02:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:01:19 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:02:33 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:03:39 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-06-22 05:02:54 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-06-22 05:03:34 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-06-22 05:01:35 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.012 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-22 05:03:07 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.041 |  |
| 2026-06-22 05:07:52 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.045 |  |
| 2026-06-22 05:01:21 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)