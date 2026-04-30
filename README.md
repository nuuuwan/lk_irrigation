# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_17:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 17:16:18 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:15:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:13:01 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-30 17:12:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:10:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.086 |  |
| 2026-04-30 17:09:56 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:09:51 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-30 17:07:08 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:07:08 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-30 17:06:44 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:06:16 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:06:07 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:05:41 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:05:38 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.019 |  |
| 2026-04-30 17:05:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-30 17:04:49 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-30 17:04:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:04:25 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 17:04:23 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-04-30 17:04:22 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:04:04 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 17:03:58 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:47 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:31 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:15 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-30 17:03:14 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-04-30 17:03:09 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:02:57 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:02:31 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:02:24 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-04-30 17:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-04-30 17:02:20 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 17:01:03 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:00:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:00:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:00:34 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 17:04:49 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-30 17:13:01 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-30 17:07:08 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-30 17:09:51 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-30 17:04:04 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-30 17:02:20 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-30 17:03:15 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-30 17:05:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-30 17:04:25 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 17:06:16 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:00:34 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:12:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:02:57 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:02:31 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:06:07 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:04:36 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:00:53 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:09 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:47 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:31 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:16:18 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:03:58 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:09:56 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:15:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:06:44 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 17:05:41 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:01:03 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:04:22 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:07:08 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:00:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-30 17:04:23 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-04-30 17:05:38 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.019 |  |
| 2026-04-30 17:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-04-30 17:03:14 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.030 |  |
| 2026-04-30 16:03:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-04-30 17:02:24 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-04-30 17:10:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)