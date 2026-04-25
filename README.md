# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_13:43:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 13:43:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-25 13:16:19 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-25 13:14:43 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.017 |  |
| 2026-04-25 13:13:14 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:11:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:10:49 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:10:16 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:09:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-04-25 13:09:39 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-04-25 13:07:31 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:06:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-25 13:05:58 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:05:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:05:38 | Katharagama (Menik Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-04-25 13:05:27 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.030 |  |
| 2026-04-25 13:05:21 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |
| 2026-04-25 13:05:10 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:04:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:04:55 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-25 13:04:26 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.023 |  |
| 2026-04-25 13:04:18 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-04-25 13:04:14 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:04:14 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:03:47 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 13:03:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-25 13:03:02 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:36 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:02:36 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:02:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:18 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:01:41 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:01:17 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:01:07 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-04-25 13:00:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:00:37 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.040 |  |
| 2026-04-25 13:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 13:43:44 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-25 13:06:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-25 13:16:19 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-25 13:03:47 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 13:04:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:11:19 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:03:02 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:04:14 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:10:49 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:04:18 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:05:10 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:02:18 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:07:31 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:05:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:01:41 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-25 13:10:16 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:05:58 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:13:14 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-04-25 13:02:36 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:04:14 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:02:36 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:00:38 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:01:17 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-04-25 13:14:43 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.017 |  |
| 2026-04-25 13:09:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-04-25 13:09:39 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-04-25 13:03:46 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-25 13:04:55 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-04-25 13:04:26 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.023 |  |
| 2026-04-25 13:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-04-25 13:05:27 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.030 |  |
| 2026-04-25 13:01:07 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-04-25 13:00:37 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.040 |  |
| 2026-04-25 13:05:38 | Katharagama (Menik Ganga) | 1.70 | 🟢 Normal | -0.043 |  |
| 2026-04-25 13:05:21 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)