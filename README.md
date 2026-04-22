# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_17:15:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 17:15:09 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:14:38 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-22 17:11:05 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:07:56 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 17:07:51 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 17:07:43 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-04-22 17:06:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:06:06 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 17:05:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:21 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 17:04:59 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:04:52 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:04:30 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 17:03:42 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:03:41 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:03:33 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 17:03:04 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:03:04 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.271 |  |
| 2026-04-22 17:03:03 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-04-22 17:02:48 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.039 |  |
| 2026-04-22 17:02:33 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.041 |  |
| 2026-04-22 17:02:33 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.548 | 🔺 Rising |
| 2026-04-22 17:02:31 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:02:28 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:02:18 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-22 17:02:10 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:02:08 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-22 17:01:58 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.052 |  |
| 2026-04-22 17:01:55 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 17:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:01:34 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 17:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-22 17:00:32 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:00:31 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.052 |  |
| 2026-04-22 17:00:16 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-04-22 17:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 17:02:33 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.548 | 🔺 Rising |
| 2026-04-22 17:04:30 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 17:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-22 17:01:55 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 17:05:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 17:07:51 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-22 17:07:56 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 17:01:34 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 17:06:06 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 17:03:33 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 17:03:42 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:01:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:15:09 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:11:05 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:04:59 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:59 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 16:02:07 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:05:21 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:03:41 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:03:04 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:02:31 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:06:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:14:38 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-22 17:04:52 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:02:10 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:02:28 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:00:16 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-04-22 17:07:43 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-04-22 16:03:26 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-22 17:03:03 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.021 |  |
| 2026-04-22 17:02:08 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-04-22 17:02:18 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-04-22 17:02:48 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.039 |  |
| 2026-04-22 17:02:33 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.041 |  |
| 2026-04-22 17:01:58 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.052 |  |
| 2026-04-22 17:00:31 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.052 |  |
| 2026-04-22 17:03:04 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)