# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_17:16:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 17:16:59 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.008 |  |
| 2026-06-30 17:16:15 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.011 |  |
| 2026-06-30 17:12:48 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:11:29 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-30 17:11:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:11:27 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-30 17:09:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:08:52 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-06-30 17:08:28 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-30 17:07:44 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.121 |  |
| 2026-06-30 17:06:31 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:06:21 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:06:07 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.041 |  |
| 2026-06-30 17:06:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-30 17:05:55 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.078 |  |
| 2026-06-30 17:05:53 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 17:04:05 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-30 17:06:01 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-30 17:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-30 17:03:27 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-30 17:08:28 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-06-30 17:02:09 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 17:03:21 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:01:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:11:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:00:45 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:11:27 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:12:48 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:06:21 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:05:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:02:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:03:40 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:00:33 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:06:31 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:09:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:02:31 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 17:16:59 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.008 |  |
| 2026-06-30 16:08:09 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.009 |  |
| 2026-06-30 17:11:29 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-30 17:03:32 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-30 17:16:15 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.011 |  |
| 2026-06-30 17:05:53 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-06-30 17:01:57 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.021 |  |
| 2026-06-30 17:03:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-06-30 17:03:20 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-06-30 17:08:52 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-06-30 17:04:59 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-06-30 17:03:48 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.040 |  |
| 2026-06-30 17:06:07 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.041 |  |
| 2026-06-30 17:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | -0.050 |  |
| 2026-06-30 17:03:12 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.050 |  |
| 2026-06-30 17:05:55 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.078 |  |
| 2026-06-30 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.099 |  |
| 2026-06-30 17:07:44 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)