# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_18:10:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 18:10:53 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:09:22 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:08:08 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-19 18:07:48 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.093 |  |
| 2026-05-19 18:06:37 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 18:05:42 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:05:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:05:12 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-19 18:04:53 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:04:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:57 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-19 18:03:49 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:45 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:16 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.029 |  |
| 2026-05-19 18:03:15 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.023 |  |
| 2026-05-19 18:03:09 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:05 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:00 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 18:02:55 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:02:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.129 |  |
| 2026-05-19 18:02:38 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:02:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:02:19 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.195 |  |
| 2026-05-19 18:02:11 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | -0.041 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 18:01:56 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:01:52 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-05-19 18:01:45 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.063 |  |
| 2026-05-19 18:01:34 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.024 |  |
| 2026-05-19 18:01:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:01:32 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:01:30 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:00:11 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:24:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 18:05:12 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-19 18:06:37 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 18:03:00 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 18:08:08 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-19 18:02:38 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 18:04:04 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-19 17:05:56 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:02:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:48 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:01:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:04:53 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:49 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:00:11 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:02:55 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:09:22 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:01:30 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:05:42 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-19 18:03:05 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:05:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:45 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:01:32 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:10:53 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:09 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.43 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:04:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:01:56 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-05-19 18:03:57 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-05-19 18:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-05-19 18:02:04 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2026-05-19 18:01:52 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-05-19 18:03:15 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.023 |  |
| 2026-05-19 18:01:34 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.024 |  |
| 2026-05-19 18:03:16 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.029 |  |
| 2026-05-19 18:02:11 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | -0.041 |  |
| 2026-05-19 18:01:45 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.063 |  |
| 2026-05-19 18:07:48 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.093 |  |
| 2026-05-19 18:02:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.129 |  |
| 2026-05-19 18:02:19 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)