# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_08:06:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,217 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 08:06:11 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-18 08:06:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.046 |  |
| 2026-04-18 08:05:52 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 08:05:51 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:05:27 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.038 |  |
| 2026-04-18 08:05:21 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-04-18 08:05:02 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-04-18 08:04:34 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:04:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:04:31 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.067 |  |
| 2026-04-18 08:04:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-18 08:03:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:03:38 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:57 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:40 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-18 08:02:28 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-18 08:02:09 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:02:01 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:53 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:43 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.043 |  |
| 2026-04-18 08:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:13 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.022 |  |
| 2026-04-18 08:01:00 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:00:53 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.053 |  |
| 2026-04-18 08:00:34 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.122 |  |
| 2026-04-18 08:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:00:16 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-18 07:20:56 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 07:16:52 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 07:14:44 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 08:02:28 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-18 08:02:40 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-18 07:09:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-18 08:04:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-18 07:14:44 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-04-18 08:05:52 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 08:06:11 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-18 08:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:04:31 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:01 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:03:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 07:01:13 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:57 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:05:51 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:03:38 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:04:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:53 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 07:07:17 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:02:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:01:00 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 08:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:04:34 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:02:09 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-18 07:03:43 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-18 08:05:02 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.019 |  |
| 2026-04-18 08:05:21 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-04-18 08:01:13 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.022 |  |
| 2026-04-18 07:02:19 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.024 |  |
| 2026-04-18 08:00:16 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-18 08:05:27 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.038 |  |
| 2026-04-18 08:01:43 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.043 |  |
| 2026-04-18 08:06:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.046 |  |
| 2026-04-18 08:00:53 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.053 |  |
| 2026-04-18 08:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | -0.067 |  |
| 2026-04-18 07:10:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.085 |  |
| 2026-04-18 07:07:40 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.113 |  |
| 2026-04-18 07:05:28 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.120 |  |
| 2026-04-18 08:00:34 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)