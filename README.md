# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_09:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 09:11:49 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:09:15 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-20 09:08:40 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:08:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:07:01 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-06-20 09:07:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-06-20 09:06:53 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.029 |  |
| 2026-06-20 09:06:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:06:22 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-20 09:05:53 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-06-20 09:05:16 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:10 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:08 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.057 |  |
| 2026-06-20 09:04:28 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:04:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:04:00 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:03:45 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:03:39 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.050 |  |
| 2026-06-20 09:03:20 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.013 |  |
| 2026-06-20 09:02:51 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:51 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:02:39 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:02:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:23 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.087 |  |
| 2026-06-20 09:02:04 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:02 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.021 |  |
| 2026-06-20 09:01:49 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:01:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:01:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:01:13 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 09:00:54 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.022 |  |
| 2026-06-20 09:00:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:00:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 09:09:15 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-20 09:06:22 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-06-20 09:01:13 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-20 09:00:24 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:04:00 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:04:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 09:00:22 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:16 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:01:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:11:49 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:08:40 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:10 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:06:27 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:08:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:32 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:04:28 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:05:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-20 08:22:09 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:51 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:02:25 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 09:07:01 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.009 |  |
| 2026-06-20 09:07:00 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-06-20 09:01:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:01:49 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:02:04 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:02:39 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 09:03:20 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.013 |  |
| 2026-06-20 09:03:39 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:02:51 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:03:45 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-06-20 09:02:02 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.021 |  |
| 2026-06-20 09:00:54 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.022 |  |
| 2026-06-20 09:05:53 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-06-20 09:06:53 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.029 |  |
| 2026-06-20 09:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | -0.050 |  |
| 2026-06-20 09:05:01 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.057 |  |
| 2026-06-20 09:02:23 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)