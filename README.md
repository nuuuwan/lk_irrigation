# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_07:42:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,576 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 07:42:41 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-08 07:33:46 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 07:29:15 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:28:36 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-08 07:26:44 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-06-08 07:13:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:11:03 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-06-08 07:09:46 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:09:06 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-06-08 07:09:04 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:08:38 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-06-08 07:08:23 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.018 |  |
| 2026-06-08 07:07:19 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.058 |  |
| 2026-06-08 07:07:12 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:06:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-06-08 07:05:56 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:05:37 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-08 07:05:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.049 |  |
| 2026-06-08 07:05:06 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.029 |  |
| 2026-06-08 07:04:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-08 07:04:10 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-06-08 07:03:57 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-06-08 07:03:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:03:10 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:45 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:02:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:02:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:03 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:01:58 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:01:25 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:01:21 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.090 |  |
| 2026-06-08 07:01:17 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.052 |  |
| 2026-06-08 07:00:40 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 07:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-06-08 07:04:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-08 07:42:41 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-08 07:05:37 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-08 07:33:46 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 07:28:36 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-08 07:05:56 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:09:46 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:02:32 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 07:01:25 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:00:40 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:03:57 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:03:10 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:03:21 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:29:15 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:07:12 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:13:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:09:04 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:02:03 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 07:26:44 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-06-08 07:11:03 | Magura (Kalu Ganga) | 2.84 | 🟢 Normal | -0.009 |  |
| 2026-06-08 07:08:38 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-06-08 07:02:45 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:01:58 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-08 07:08:23 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.018 |  |
| 2026-06-08 07:09:06 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-06-08 07:05:06 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.029 |  |
| 2026-06-08 07:05:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.049 |  |
| 2026-06-08 07:04:10 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.049 |  |
| 2026-06-08 07:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-06-08 07:01:17 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | -0.052 |  |
| 2026-06-08 07:07:19 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.058 |  |
| 2026-06-08 07:06:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.059 |  |
| 2026-06-08 07:01:21 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)