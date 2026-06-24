# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_01:40:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,548 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 01:40:02 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:34:12 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:24:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -1.029 |  |
| 2026-06-25 01:24:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -1.029 |  |
| 2026-06-25 01:22:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.55 | 🟢 Normal | -1.029 |  |
| 2026-06-25 01:20:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-06-25 01:14:37 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:13:02 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-25 01:10:39 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:09:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:09:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.244 |  |
| 2026-06-25 01:08:38 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-06-25 01:07:39 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:07:19 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.029 |  |
| 2026-06-25 01:06:41 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:06:21 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:06:13 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:46 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.033 |  |
| 2026-06-25 01:04:36 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:24 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:04:09 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:04:02 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-25 01:03:52 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-06-25 01:03:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:03:29 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:02:01 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-06-25 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:01:07 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:00:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 00:02:46 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:03:45 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:06:13 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:05:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:19 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:03:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:36 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:34:12 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:06:21 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:14:37 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:09:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:03:29 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:04:48 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:10:39 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:07:39 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:40:02 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:06:41 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 01:13:02 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-25 01:08:38 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:13:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-06-25 01:04:10 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:01:07 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:04:09 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-25 01:03:52 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-06-25 00:07:58 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-06-25 01:04:02 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-25 01:07:19 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.029 |  |
| 2026-06-25 01:02:01 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-06-25 01:04:46 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.033 |  |
| 2026-06-25 00:02:46 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.039 |  |
| 2026-06-25 00:06:06 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-06-25 01:20:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.050 |  |
| 2026-06-25 01:09:26 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.244 |  |
| 2026-06-25 01:24:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -1.029 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)