# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_15:23:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 15:23:00 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.046 |  |
| 2026-04-30 15:18:25 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:18:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:15:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:12:15 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-04-30 15:10:52 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:10:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.079 |  |
| 2026-04-30 15:10:35 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:09:55 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-04-30 15:09:35 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-30 15:07:03 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.019 |  |
| 2026-04-30 15:05:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:04:53 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:04:37 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:04:26 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-30 15:04:19 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.057 |  |
| 2026-04-30 15:04:14 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:03:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:03:53 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-30 15:03:39 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-04-30 15:03:37 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:03:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-04-30 15:03:18 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:03:16 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:03:15 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:02:56 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:02:55 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:02:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 15:02:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:02:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:02:29 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 15:02:24 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:02:07 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-04-30 15:01:46 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-04-30 15:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:01:12 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 15:01:11 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:00:35 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:00:28 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:59:50 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 15:02:29 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 15:04:26 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-30 15:02:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 15:09:35 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-30 15:01:12 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 15:02:55 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:02:45 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:10:52 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:18:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:03:16 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:05:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:02:24 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:18:25 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 14:59:50 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:04:53 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:03:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:10:35 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:04:37 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:00:28 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:15:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:09:55 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-04-30 15:03:15 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:02:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:00:35 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:02:56 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:04:14 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:03:18 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:01:11 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:12:15 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-04-30 15:07:03 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.019 |  |
| 2026-04-30 15:03:53 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-30 15:02:07 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-04-30 15:03:39 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-04-30 15:01:46 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.029 |  |
| 2026-04-30 15:03:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-04-30 15:23:00 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.046 |  |
| 2026-04-30 15:04:19 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.057 |  |
| 2026-04-30 15:10:45 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)