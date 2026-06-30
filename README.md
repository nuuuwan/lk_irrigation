# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_06:41:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 06:41:22 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.001 |  |
| 2026-06-30 06:17:21 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-06-30 06:14:26 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:11:26 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:09:47 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | -0.028 |  |
| 2026-06-30 06:09:41 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-06-30 06:09:27 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.246 |  |
| 2026-06-30 06:08:34 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.091 |  |
| 2026-06-30 06:08:10 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-06-30 06:07:56 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:07:25 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-30 06:06:30 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.059 |  |
| 2026-06-30 06:05:53 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:05:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:05:15 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 06:04:56 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.133 |  |
| 2026-06-30 06:04:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.035 |  |
| 2026-06-30 06:04:12 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-06-30 06:03:52 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.124 |  |
| 2026-06-30 06:03:47 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 06:03:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 06:03:36 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-06-30 06:03:31 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.453 |  |
| 2026-06-30 06:03:22 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:55 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:45 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:02:45 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:36 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-06-30 06:02:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:12 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-06-30 06:02:02 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:01:53 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.207 |  |
| 2026-06-30 06:01:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:01:17 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.215 |  |
| 2026-06-30 06:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-06-30 06:00:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:00:37 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 06:00:18 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 06:09:41 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-06-30 06:07:25 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-30 06:00:37 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-30 06:05:15 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 06:03:47 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 06:02:02 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:02:45 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:01:43 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:03:31 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 06:02:45 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:03:22 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:00:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:01:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:05:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:11:26 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:14:26 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:02:55 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:07:56 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-30 06:41:22 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.001 |  |
| 2026-06-30 06:03:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-30 06:02:12 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-06-30 06:03:36 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-06-30 06:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-06-30 06:09:47 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | -0.028 |  |
| 2026-06-30 06:04:12 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.029 |  |
| 2026-06-30 06:02:36 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-06-30 06:04:28 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.035 |  |
| 2026-06-30 06:08:10 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-06-30 06:17:21 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-06-30 06:06:30 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | -0.059 |  |
| 2026-06-30 06:08:34 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.091 |  |
| 2026-06-30 06:03:52 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.124 |  |
| 2026-06-30 06:04:56 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.133 |  |
| 2026-06-30 06:01:53 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.207 |  |
| 2026-06-30 06:01:17 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.215 |  |
| 2026-06-30 06:09:27 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.246 |  |
| 2026-06-30 06:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.453 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)