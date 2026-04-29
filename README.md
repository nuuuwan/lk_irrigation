# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_02:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 02:11:15 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:11:12 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-30 02:11:11 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-30 02:09:38 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 02:08:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:07:40 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 02:06:28 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 02:05:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-30 02:05:13 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -1.500 |  |
| 2026-04-30 02:04:05 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-30 02:03:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:53 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:37 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -1.500 |  |
| 2026-04-30 02:03:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:02:59 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-30 02:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-04-30 02:02:41 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-30 02:02:32 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.119 |  |
| 2026-04-30 02:02:28 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:02:18 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-04-30 02:01:34 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.083 |  |
| 2026-04-30 02:01:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.043 |  |
| 2026-04-30 02:01:11 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.055 |  |
| 2026-04-30 02:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:00:50 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.050 |  |
| 2026-04-30 02:00:37 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-30 02:00:21 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-04-30 01:59:39 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:42:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 01:33:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 02:11:12 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-04-30 01:20:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-30 02:00:37 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-30 02:04:05 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-30 02:02:41 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-30 02:05:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-30 02:02:59 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 02:06:28 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 02:09:38 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 02:07:40 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 01:42:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 02:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:53 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:59:39 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:02:01 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:02:18 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:03:58 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:08:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:02:28 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 02:11:15 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:12:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 01:09:32 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-04-30 02:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-04-30 01:03:44 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 01:15:27 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.017 |  |
| 2026-04-30 02:00:21 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-04-30 02:01:12 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.043 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-30 02:00:50 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.050 |  |
| 2026-04-30 02:01:11 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.055 |  |
| 2026-04-30 02:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-04-30 00:05:07 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.060 |  |
| 2026-04-30 01:07:52 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-04-30 02:01:34 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.083 |  |
| 2026-04-30 02:02:32 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.119 |  |
| 2026-04-30 02:05:13 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)