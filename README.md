# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_12:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,052 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 12:13:31 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:09:19 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.018 |  |
| 2026-02-21 12:08:49 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:08:38 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-02-21 12:06:49 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:06:45 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.065 |  |
| 2026-02-21 12:06:24 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-21 12:06:13 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:52 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-02-21 12:05:44 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:35 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:24 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:14 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 12:05:07 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:03 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-02-21 12:05:01 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-02-21 12:04:13 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:04:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:03:53 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:03:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:03:35 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:03:27 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:03:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:03:17 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-02-21 12:03:15 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:03:01 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:02:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:45 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:41 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-02-21 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-02-21 12:02:06 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:01:49 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:01:37 | Manampitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.040 |  |
| 2026-02-21 12:01:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-02-21 12:00:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-21 12:00:26 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.151 |  |
| 2026-02-21 12:00:25 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 12:05:03 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-02-21 12:06:24 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-02-21 12:05:14 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-21 12:00:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-21 12:02:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:04:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:45 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:06:13 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:07 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:35 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:05:44 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:03:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:06:49 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:01:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:13:31 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:02:06 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 12:03:15 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:04:13 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:03:51 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:03:53 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:01:49 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:08:49 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.010 |  |
| 2026-02-21 12:09:19 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.018 |  |
| 2026-02-21 12:05:52 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-02-21 12:03:27 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:00:25 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:03:35 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:03:01 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-21 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | -0.021 |  |
| 2026-02-21 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-02-21 12:02:41 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-02-21 12:05:01 | Padiyathalawa (Maduru Oya) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-02-21 12:03:17 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-02-21 12:01:37 | Manampitiya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.040 |  |
| 2026-02-21 12:08:38 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.049 |  |
| 2026-02-21 12:06:45 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.065 |  |
| 2026-02-21 12:00:26 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)