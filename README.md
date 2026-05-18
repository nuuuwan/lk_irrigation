# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_07:35:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 07:35:53 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:32:29 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-05-18 07:24:57 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-05-18 07:18:08 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:17:26 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.016 |  |
| 2026-05-18 07:16:15 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-05-18 07:13:51 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-05-18 07:13:33 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:13:23 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.050 |  |
| 2026-05-18 07:10:59 | Putupaula (Kalu Ganga) | 2.22 | 🟢 Normal | -0.043 |  |
| 2026-05-18 07:10:40 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.056 |  |
| 2026-05-18 07:08:03 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-05-18 07:06:54 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.060 |  |
| 2026-05-18 07:06:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.122 |  |
| 2026-05-18 07:06:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:06:03 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:15 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:13 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:05 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:03 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:04:51 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.090 |  |
| 2026-05-18 07:04:38 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:04:32 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:04:28 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:04:11 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:03:45 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:03:27 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.078 |  |
| 2026-05-18 07:03:12 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:03:04 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:02:25 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-05-18 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | -0.039 |  |
| 2026-05-18 07:02:15 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:02:15 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | -0.060 |  |
| 2026-05-18 07:02:10 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-18 07:02:05 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:01:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:01:19 | Thanthirimale (Malwathu Oya) | 3.32 | 🟢 Normal | -0.023 |  |
| 2026-05-18 07:01:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-18 07:00:55 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:00:53 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-05-18 07:00:47 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | -0.039 |  |
| 2026-05-18 07:16:15 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-05-18 07:01:18 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-18 07:05:15 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:13:33 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:04:11 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:35:53 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:00:47 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:02:15 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:06:03 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:13 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:00:55 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:06:23 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:18:08 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:04:32 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:05:05 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:01:29 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-18 07:24:57 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.014 |  |
| 2026-05-18 07:17:26 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.016 |  |
| 2026-05-18 07:03:04 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:05:03 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:03:45 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-18 07:32:29 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-05-18 07:01:19 | Thanthirimale (Malwathu Oya) | 3.32 | 🟢 Normal | -0.023 |  |
| 2026-05-18 07:08:03 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-05-18 07:04:38 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:04:28 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:02:05 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.029 |  |
| 2026-05-18 07:02:10 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.032 |  |
| 2026-05-18 07:10:59 | Putupaula (Kalu Ganga) | 2.22 | 🟢 Normal | -0.043 |  |
| 2026-05-18 07:00:53 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.048 |  |
| 2026-05-18 07:02:25 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-05-18 07:13:23 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.050 |  |
| 2026-05-18 07:10:40 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.056 |  |
| 2026-05-18 07:02:15 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | -0.060 |  |
| 2026-05-18 07:06:54 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.060 |  |
| 2026-05-18 07:03:27 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.078 |  |
| 2026-05-18 07:04:51 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.090 |  |
| 2026-05-18 07:06:51 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)