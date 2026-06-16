# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_04:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 04:15:19 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-17 04:13:46 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.027 |  |
| 2026-06-17 04:10:17 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:09:34 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:09:19 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.019 |  |
| 2026-06-17 04:09:04 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:06:39 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-06-17 04:06:38 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:06:16 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:06:10 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:05:52 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.019 |  |
| 2026-06-17 04:05:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2026-06-17 04:05:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:05:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:04:26 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:03:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:03:12 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:03:00 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-17 04:02:59 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 04:02:38 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-17 04:02:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:32 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:31 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.036 |  |
| 2026-06-17 04:02:29 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:54 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.292 |  |
| 2026-06-17 04:01:52 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:16 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 02:03:32 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-17 03:11:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-17 04:02:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 03:08:11 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:03:12 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:32 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:06 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:06:16 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:16 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-17 03:09:33 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:03:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:11 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:06:38 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:05:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:05:13 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:10:17 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 02:08:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:01:52 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:02:29 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 04:06:39 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-06-17 03:05:03 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-17 04:15:19 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-17 04:02:38 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-17 04:03:00 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-06-17 04:09:19 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.019 |  |
| 2026-06-17 04:05:52 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.019 |  |
| 2026-06-17 04:09:04 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:06:10 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:02:59 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-06-17 04:13:46 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.027 |  |
| 2026-06-17 03:04:23 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-17 04:02:31 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.036 |  |
| 2026-06-17 03:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.040 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-17 04:05:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2026-06-17 04:01:54 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)