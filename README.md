# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_00:11:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 00:11:51 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2026-04-25 00:09:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:08:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-04-25 00:06:48 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 00:06:25 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-04-25 00:05:43 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-04-25 00:05:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-04-25 00:04:42 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-25 00:04:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-25 00:04:02 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.019 |  |
| 2026-04-25 00:03:54 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.049 |  |
| 2026-04-25 00:03:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-25 00:03:15 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:03:15 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-04-25 00:02:51 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 00:02:41 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:33 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:30 | Katharagama (Menik Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-04-25 00:02:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-25 00:02:24 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:05 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.094 |  |
| 2026-04-25 00:01:39 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:37 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-25 00:01:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.069 |  |
| 2026-04-25 00:01:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:09 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:00:33 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 23:26:24 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 86.087 | 🔺 Rising |
| 2026-04-25 00:02:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-25 00:04:42 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 23:26:24 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 00:02:51 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 00:01:39 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:41 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:33 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:08:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:28 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:02:24 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:09:08 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:11:51 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:00:33 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:01:09 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 00:07:05 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-04-25 00:03:46 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-24 23:03:32 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-25 00:01:37 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-25 00:02:30 | Katharagama (Menik Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-04-24 23:02:23 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-04-25 00:05:43 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-04-25 00:05:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-04-25 00:04:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-25 00:04:02 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | -0.019 |  |
| 2026-04-25 00:06:48 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 00:06:25 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 00:03:15 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-04-24 23:02:52 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.033 |  |
| 2026-04-25 00:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2026-04-25 00:03:54 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.049 |  |
| 2026-04-24 23:09:06 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.055 |  |
| 2026-04-25 00:01:33 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.069 |  |
| 2026-04-25 00:02:05 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.094 |  |
| 2026-04-24 22:17:29 | Wellawaya (Kirindi Oya) | 0.18 | 🟢 Normal | -8.018 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)