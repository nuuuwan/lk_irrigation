# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_00:27:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 00:27:29 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-06 00:16:53 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.009 |  |
| 2026-06-06 00:13:32 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-06 00:09:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-06-06 00:07:06 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-06-06 00:06:57 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.039 |  |
| 2026-06-06 00:06:37 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-06 00:06:06 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:05:45 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-06 00:05:02 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-06 00:04:58 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:04:56 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 00:04:52 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-06 00:04:41 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:04:27 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.146 |  |
| 2026-06-06 00:04:25 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-06 00:04:09 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-06 00:03:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:03:53 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.019 |  |
| 2026-06-06 00:03:49 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 00:03:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:03:20 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 00:03:00 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-06 00:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.014 |  |
| 2026-06-06 00:02:50 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-06 00:02:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:01:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:01:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-06 00:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-06 00:01:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:59:08 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 00:04:09 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-06-06 00:05:02 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-06 00:04:52 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-06-06 00:27:29 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-06 00:04:25 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-05 21:16:46 | Putupaula (Kalu Ganga) | 1.61 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-06 00:03:36 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 00:03:20 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 00:05:45 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-06 00:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 18:01:21 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 00:04:56 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 00:03:49 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:06:06 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:01:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:03:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:02:50 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:00:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-05 18:06:46 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:04:41 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:03:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:02:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:04:58 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-05 23:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:01:44 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 00:16:53 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.009 |  |
| 2026-06-06 00:13:32 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.009 |  |
| 2026-06-06 00:01:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-05 23:01:18 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-06 00:03:00 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-06 00:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.014 |  |
| 2026-06-06 00:03:53 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.019 |  |
| 2026-06-05 18:01:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-06-06 00:06:37 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-06 00:09:10 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-06-06 00:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-06 00:06:57 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.039 |  |
| 2026-06-06 00:07:06 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.058 |  |
| 2026-06-06 00:04:27 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)