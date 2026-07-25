# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_07:10:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 07:10:40 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:09:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-07-25 07:09:01 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-25 07:08:08 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:06:57 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-07-25 07:06:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:05:11 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-25 07:05:02 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.013 |  |
| 2026-07-25 07:04:56 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:04:47 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-25 07:04:30 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.050 |  |
| 2026-07-25 07:04:27 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:04:23 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-25 07:04:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:03:22 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:03:21 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:03:20 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.048 |  |
| 2026-07-25 07:02:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-25 07:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-07-25 07:02:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:31 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:29 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:27 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.001 |  |
| 2026-07-25 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-07-25 07:02:10 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:09 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:08 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:02 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:40 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:20 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:05 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-07-25 07:00:15 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-25 06:30:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.001 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 07:02:53 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-07-25 07:00:15 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-25 07:09:01 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-25 07:04:23 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-25 07:02:27 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.001 |  |
| 2026-07-25 07:01:20 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:31 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:08 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:08:08 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:29 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:03:21 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:10 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:40 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 06:02:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:03:22 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:04:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:06:51 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-25 06:04:37 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:04:27 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:02:09 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:04:56 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:01:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-25 06:04:43 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-25 06:01:36 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-25 07:10:40 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 06:30:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.001 |  |
| 2026-07-25 07:09:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-07-25 07:06:57 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-07-25 07:05:11 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-07-25 07:04:47 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-25 07:05:02 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.013 |  |
| 2026-07-25 07:01:05 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-07-25 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-07-25 07:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-07-25 07:03:20 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.048 |  |
| 2026-07-25 07:04:30 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.050 |  |
| 2026-07-25 06:04:11 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)