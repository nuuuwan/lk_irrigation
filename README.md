# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_07:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 07:16:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.066 |  |
| 2026-04-22 07:15:37 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-04-22 07:13:39 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-22 07:11:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-04-22 07:10:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.025 |  |
| 2026-04-22 07:06:54 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.132 |  |
| 2026-04-22 07:06:42 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-04-22 07:06:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.448 | 🔺 Rising |
| 2026-04-22 07:05:53 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.081 |  |
| 2026-04-22 07:05:30 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-22 07:05:29 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-04-22 07:05:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-04-22 07:04:49 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:04:38 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 07:03:48 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 07:03:46 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-22 07:03:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:03:30 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-04-22 07:03:14 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-22 07:03:08 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 07:02:49 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.121 |  |
| 2026-04-22 07:02:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:02:44 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-22 07:02:42 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-04-22 07:02:34 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.060 |  |
| 2026-04-22 07:02:15 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:02:08 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.072 |  |
| 2026-04-22 07:02:07 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-22 07:02:04 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-04-22 07:01:53 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.002 |  |
| 2026-04-22 07:01:43 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.116 |  |
| 2026-04-22 07:01:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.051 |  |
| 2026-04-22 07:01:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:01:33 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:01:08 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 07:00:36 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-04-22 06:46:23 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 07:06:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.448 | 🔺 Rising |
| 2026-04-22 07:03:14 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-22 07:01:08 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 07:02:44 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-22 07:13:39 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-22 07:02:07 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-22 07:03:08 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 07:03:48 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 07:04:38 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 07:01:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:03:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 05:11:18 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:01:33 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:04:49 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 07:01:53 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.002 |  |
| 2026-04-22 07:02:15 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:02:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:05:53 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-04-22 07:03:46 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-22 07:02:42 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-04-22 07:05:29 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-04-22 07:15:37 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-04-22 07:03:30 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.019 |  |
| 2026-04-22 07:05:30 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-04-22 07:00:36 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-04-22 07:10:32 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.025 |  |
| 2026-04-22 07:06:42 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2026-04-22 07:01:43 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.051 |  |
| 2026-04-22 07:02:04 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-04-22 07:02:34 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.060 |  |
| 2026-04-22 07:11:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-04-22 07:16:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.066 |  |
| 2026-04-22 06:00:25 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.071 |  |
| 2026-04-22 07:02:08 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.072 |  |
| 2026-04-22 07:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.081 |  |
| 2026-04-22 07:05:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-04-22 07:01:43 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.116 |  |
| 2026-04-22 07:02:49 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.121 |  |
| 2026-04-22 07:06:54 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)