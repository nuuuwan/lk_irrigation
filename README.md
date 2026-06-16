# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_11:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,859 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 11:10:18 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-06-16 11:09:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:09:08 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:08:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-16 11:08:07 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-06-16 11:07:39 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:07:28 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.005 |  |
| 2026-06-16 11:06:13 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.029 |  |
| 2026-06-16 11:06:08 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-06-16 11:05:42 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:05:36 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:05:25 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-16 11:05:16 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.022 |  |
| 2026-06-16 11:04:53 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:03:46 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 11:03:40 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:03:39 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.021 |  |
| 2026-06-16 11:03:30 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:03:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:03:03 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:02:55 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 11:02:49 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:02:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:02:28 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:02:19 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:02:14 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-16 11:02:11 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-06-16 11:02:02 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:01:43 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:01:42 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:01:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-06-16 11:00:59 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:30 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 11:08:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-16 11:05:25 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-16 11:02:55 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 11:03:46 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 11:02:19 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:02:28 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:02:02 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 11:00:30 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:03:03 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:03:30 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:05:42 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:03:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:43 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:00:59 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:02:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:05:36 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:07:39 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:42 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:09:08 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:09:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:01:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-16 11:07:28 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.005 |  |
| 2026-06-16 11:03:40 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:04:53 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:02:49 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:01:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-06-16 11:10:18 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-06-16 11:02:14 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.020 |  |
| 2026-06-16 11:02:11 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-06-16 11:03:39 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.021 |  |
| 2026-06-16 11:08:07 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-06-16 11:05:16 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.022 |  |
| 2026-06-16 11:06:13 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.029 |  |
| 2026-06-16 11:06:08 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-06-16 11:01:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)